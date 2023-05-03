from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from .models import Temporary


class YourModelTestCase(TestCase):
    class TemporaryTestCase(TestCase):
        def test_temporary_deletion(self):
            # Создаем временную запись
            temporary = Temporary.objects.create(name='test',
                                                 expiration_date=timezone.now() + timezone.timedelta(days=1))

            # Удаляем временную запись
            temporary.delete()

            # Проверяем, что временная запись удалена
            self.assertFalse(Temporary.objects.filter(pk=temporary.pk).exists())
