from django.contrib.auth import get_user_model
from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка клиентов и обновления
    """

    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'username',
            'status',
        )


class ClientCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'password_confirm',
            'status',
        )
        read_only_fields = ('id',)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password', 'password_confirm')
        }
        data['password'] = validated_data['password_confirm']
        return self.Meta.model.objects.create_user(**data)
