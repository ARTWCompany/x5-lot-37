from django.contrib.auth.models import AbstractUser
from django.db import models

from common.constants import StatusChoices


class Client(AbstractUser):
    """
    Модель клиентов API
    """

    status = models.CharField(
        max_length=70,
        choices=StatusChoices.choices,
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'Клиент API'
        verbose_name_plural = 'Клиенты API'

    def __str__(self):
        return self.username
