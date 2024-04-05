from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from api.filters import CustomUserFilterSet
from api.serializers import (
    CustomUserSerializer,
    CustomUserCommunicationSerializer,
)
from common.constants import StatusChoices
from users.models import CustomUser, CustomUserCommunication


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка пользователей.",
    ),
    retrieve=extend_schema(
        summary='Получение пользователя по id.',
    ),
    create=extend_schema(
        summary="Создание пользователя.",
    ),
    update=extend_schema(
        summary="Изменение пользователя по id. Все поля.",
    ),
)
class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filterset_class = CustomUserFilterSet


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка пользователей доступных для коммуникации.",
    ),
)
class CustomUserCommunicationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = CustomUserCommunicationSerializer
    queryset = CustomUserCommunication.objects.filter(status=StatusChoices.ACTIVE)
