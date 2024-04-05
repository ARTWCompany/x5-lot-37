from django.db import models

from common.constants import StatusChoices


class CustomUser(models.Model):
    """
    Модель кастомного юзера
    """

    name = models.CharField(max_length=70, verbose_name='Имя')
    surname = models.CharField(max_length=70, verbose_name='Фамилия')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Адрес электронной почты')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.name} {self.surname}'


class CustomUserCommunication(models.Model):
    """
    Модель коммуникаций пользователя
    """

    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_communications',
        verbose_name='Пользователь'
    )
    blocked_from = models.DateTimeField(verbose_name='Дата блокировки')
    blocked_to = models.DateTimeField(verbose_name='Дата окончания блокировки')
    status = models.CharField(
        max_length=70,
        choices=StatusChoices.choices,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Доступность для коммуникации'
        verbose_name_plural = 'Доступность для коммуникации'

    def __str__(self):
        return self.user.name
