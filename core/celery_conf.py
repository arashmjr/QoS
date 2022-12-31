import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app_celery = Celery("back")

app_celery.autodiscover_tasks()

app_celery.conf.broker_url = "amqp://"
# if you want to execute on server use below broker_url
# app_celery.conf.broker_url = "amqp://username:password@ip_address:port"

# app_celery.conf.result_backend = "rpc://"
app_celery.conf.task_serializer = "pickle"
app_celery.conf.result_serializer = "pickle"
app_celery.conf.accept_content = ["json", "pickle"]
app_celery.conf.result_expires = timedelta(days=1)
app_celery.conf.task_always_eager = False
app_celery.conf.worker_prefetch_multiplier = 4
