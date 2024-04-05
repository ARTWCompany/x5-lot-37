from django.db import models


class StatusChoices(models.TextChoices):
    ACTIVE = 'active', 'активен'
    BLOCKED = 'blocked', 'заблокирован'


class CommunicationStatusChoices(models.TextChoices):
    SEND = 'send', 'отправлено'
    FAILED = 'failed', 'не отправлено'
    RESERVED = 'reserved', 'забронировано'
