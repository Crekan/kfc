from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from .models import Temporary


class YourModelTestCase(TestCase):
    class TemporaryTestCase(TestCase):
        def test_temporary_deletion(self):
            temporary = Temporary.objects.create(name='test',
                                                 expiration_date=timezone.now() + timezone.timedelta(days=7))

            temporary.delete()

            self.assertFalse(Temporary.objects.filter(pk=temporary.pk).exists())
