from django.db import models

from common.constants import CommunicationStatusChoices
from .abstract import CommunicationAbstract


class CommunicationKind(CommunicationAbstract):
    """
    Модель типа коммуникации
    """

    class Meta:
        verbose_name = 'Тип коммуникации'
        verbose_name_plural = 'Типы коммуникации'


class CommunicationSource(CommunicationAbstract):
    """
    Модель канала коммуникации
    """

    class Meta:
        verbose_name = 'Тип коммуникации'
        verbose_name_plural = 'Типы коммуникации'


class Communication(CommunicationAbstract):
    """
    Модель коммуникации
    """

    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='communications',
        verbose_name='Пользователь',
    )
    communication_kind = models.ForeignKey(
        'communications.CommunicationKind',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='communications',
        verbose_name='Тип коммуникации',
    )
    communication_source = models.ForeignKey(
        'communications.CommunicationSource',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='communications',
        verbose_name='Канал коммуникации',
    )
    message = models.TextField(verbose_name='Текст сообщения', default="")
    communication_date = models.DateTimeField(verbose_name='Дата коммуникации')
    status = models.CharField(
        max_length=30,
        choices=CommunicationStatusChoices.choices,
        verbose_name='Статус'
    )
    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='communications',
        verbose_name='Департамент'
    )

    class Meta:
        verbose_name = 'Коммуникация'
        verbose_name_plural = 'Коммуникации'

    def __str__(self):
        return f'{self.communication_kind} - {self.communication_source}'


class FavoriteSource(models.Model):
    """
    Модель для предпочитаемых каналов связи
    """

    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='favorites',
        verbose_name='Подразделение',
    )
    communication_type = models.ForeignKey(
        'communications.CommunicationKind',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='favorites',
        verbose_name='Тип коммуникации'
    )
    communication_source = models.ForeignKey(
        'communications.CommunicationSource',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='favorites',
        verbose_name='Канал коммуникации'
    )

    class Meta:
        verbose_name = 'Предпочитаемый канал связи'
        verbose_name_plural = 'Предпочитаемые каналы связи'

    def __str__(self):
        return f'Предпочитаемый канал {self.communication_source.name}'
