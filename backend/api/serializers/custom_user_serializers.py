from rest_framework import serializers

from users.models import CustomUser, CustomUserCommunication


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя
    """

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserCommunicationSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя
    """

    class Meta:
        model = CustomUserCommunication
        fields = '__all__'
