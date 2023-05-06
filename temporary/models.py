from django.db import models
from django.utils import timezone

from users.models import User


class YourModelManager(models.Manager):
    def records_to_delete(self):
        return self.filter(date_add__lte=timezone.now() - timezone.timedelta(days=7))


class Temporary(models.Model):
    DAY_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Восересенье', 'Восересенье'),
    )
    SHIFT_CHOICES = (
        ('FT', 'FT'),
        ('Первая смена', 'Первая смена'),
        ('Вторая смена', 'Вторая смена'),
        ('Выходной', 'Выходной'),
        ('Другое', 'Другое'),
    )
    day = models.CharField(choices=DAY_CHOICES, max_length=20)
    shift_type = models.CharField(max_length=30, choices=SHIFT_CHOICES)
    custom_time = models.CharField(max_length=255, null=True, blank=True)
    date_add = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    night = models.BooleanField(default=False)

    objects = YourModelManager()

    def __str__(self):
        return f'{self.day} - {self.shift_type}'

    def should_be_deleted(self):
        return self.date_add <= timezone.now() - timezone.timedelta(days=7)
