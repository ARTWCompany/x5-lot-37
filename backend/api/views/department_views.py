from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from api.serializers.department_serializers import (
    DepartmentSerializer,
    DepartmentCommunicationSerializer,
)
from departments.models import Department, DepartmentCommunication


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка департаментов.",
    ),
    create=extend_schema(
        summary="Создание департамента.",
    ),
)
class DepartmentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка правил для коммуникации для департамента",
    ),
    create=extend_schema(
        summary="Создание правил коммуникации для департамента.",
    ),
)
class DepartmentCommunicationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = DepartmentCommunicationSerializer
    queryset = DepartmentCommunication.objects.all()
