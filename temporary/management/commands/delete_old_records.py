from django.core.management.base import BaseCommand
from temporary.models import Temporary


class Command(BaseCommand):
    help = 'Delete old records from YourModel'

    def handle(self, *args, **options):
        old_records = Temporary.objects.old_records()
        old_records.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted old records'))
