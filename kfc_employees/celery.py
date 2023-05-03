import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kfc_employees.settings')

app = Celery('kfc_employees')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
