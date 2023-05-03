from django.db import models
from django.utils import timezone

from users.models import User


class YourModelManager(models.Manager):
    def records_to_delete(self):
        return self.filter(date_add__lte=timezone.now() - timezone.timedelta(days=7))


class Temporary(models.Model):
    DAY_CHOICES = (
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Восересенье'),
    )
    SHIFT_CHOICES = (
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
        ('other', 'Other'),
    )
    day = models.CharField(choices=DAY_CHOICES, max_length=3)
    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    custom_time = models.CharField(max_length=255, null=True, blank=True)
    date_add = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = YourModelManager()

    def __str__(self):
        return f'{self.day} - {self.shift_type}'

    def should_be_deleted(self):
        return self.date_add <= timezone.now() - timezone.timedelta(days=7)
