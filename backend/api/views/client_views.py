from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.permissions import ClientPermissions
from api.serializers.auth_serializer import (
    ClientSerializer,
)
from api.serializers.client_serializers import ClientCreateSerializer
from common.constants import StatusChoices


@extend_schema_view(
    list=extend_schema(
        request=None,
        summary='Получение списка активных клиентов API.',
        description='Клиенты имеют доступ к методам API.'
        ),
    retrieve=extend_schema(
        summary='Получение клиента по id.',
    ),
    update=extend_schema(
        summary='Изменение клиента API. Все поля.',
    ),
)
class ClientViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = ClientSerializer
    queryset = get_user_model().objects.filter(status=StatusChoices.ACTIVE)
    permission_classes = (IsAuthenticated, ClientPermissions,)


@extend_schema_view(
    create=extend_schema(
        summary='Создание нового клиента',
        description='Метод создания нового клиента.',
    ),
)
class SignUpView(generics.CreateAPIView):

    serializer_class = ClientCreateSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
