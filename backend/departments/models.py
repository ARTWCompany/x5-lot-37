from django.db import models

from departments.querysets import DepartmentCommunicationQuerySet


class Department(models.Model):
    """
    Модель подразделений
    """

    name = models.CharField(max_length=70, verbose_name='Название')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class DepartmentCommunication(models.Model):
    """
    Модель правил коммуникации
    """

    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rules',
        verbose_name='Подразделение'
    )
    limit_per_unit = models.IntegerField(
        verbose_name='Количество коммуникаций за единицу времени'
    )
    unit = models.CharField(max_length=30, verbose_name='Единица времени')
    units_count = models.IntegerField(verbose_name='Количество коммуникаций за единицу времени')

    objects = DepartmentCommunicationQuerySet.as_manager()

    class Meta:
        verbose_name = 'Правило коммуникации'
        verbose_name_plural = 'Правила коммуникации'

    def __str__(self):
        return f'{self.unit} - {self.units_count} - {self.limit_per_unit}'
