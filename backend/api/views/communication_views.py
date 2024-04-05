from django.db.models import Sum
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.serializers.comminication_serializers import (
    CommunicationKindSerializer,
    CommunicationSerializer,
    CommunicationSourceSerializer,
    CommunicationBookingSerializer,
)
from common.constants import StatusChoices, CommunicationStatusChoices
from communications.models import CommunicationKind, Communication
from departments.models import DepartmentCommunication


@extend_schema_view(
    list=extend_schema(
        request=None,
        summary='Получение списка активных типов коммуникаций.',
    ),
    create=extend_schema(
        summary='Создание типа коммуникации',
    ),
)
class CommunicationKindViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = CommunicationKindSerializer
    queryset = CommunicationKind.objects.filter(status=StatusChoices.ACTIVE)


@extend_schema_view(
    list=extend_schema(
        request=None,
        summary='Получение списка активных каналов коммуникаций.',
    ),
    create=extend_schema(
        summary='Создание канала коммуникации.',
    ),
)
class CommunicationSourceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = CommunicationSourceSerializer
    queryset = CommunicationKind.objects.filter(status=StatusChoices.ACTIVE)


@extend_schema_view(
    list=extend_schema(
        request=None,
        summary='Получение списка активных каналов коммуникаций.',
    ),
    create=extend_schema(
        summary='Создание коммуникации',
        description=(
                """
                При создании коммуникации, учитывается количество коммуникаций 
                пользователя в департаменте в единицу времени.
                В случае превышения лимита, статус коммуникации 'не отправлено'. Для дальнейшей 
                обработки таких коммуникаций можно использовать периодические асинхронные задачи.
                """
        )
    ),
    update=extend_schema(
        summary='Обновление коммуникации по id.'
    )
)
class CommunicationViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = CommunicationSerializer
    queryset = Communication.objects.all()

    def create(self, request, *args, **kwargs):
        data = self.request.data
        department_id = data.get('department')
        department_queryset = (
            DepartmentCommunication.objects
            .filter(department_id=department_id)
        )
        base_limit_rate = department_queryset.first().limit_per_unit
        amount_current_limit_rate = (
            department_queryset
            .annotate_current_limit_rate()
            .aggregate(amount_limit_rate=Sum('current_limit_rate'))
        ).get('amount_limit_rate') or 0
        if base_limit_rate and base_limit_rate < amount_current_limit_rate:
            data.update(status=CommunicationStatusChoices.FAILED)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=CommunicationBookingSerializer,
        summary='Создание отложенной коммуникации',
        description=(
            """
            Отложенная коммуникация имеет будущее время и создается со статусом 'забронировано'.
            """
        )
    )
    @action(detail=False, methods=['post'], url_path='booking')
    def booking(self, request):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == 'booking':
            return CommunicationBookingSerializer
        return CommunicationSerializer
