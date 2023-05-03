from celery import shared_task

from .models import Temporary


@shared_task
def delete_old_records():
    records_to_delete = Temporary.objects.records_to_delete()
    for record in records_to_delete:
        if record.should_be_deleted():
            record.delete()
