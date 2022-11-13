import requests
from django.utils import timezone
from src.apps.reminders.models import Reminder


def telegram_alert(data):
    headers = {"Content-type": "application/json"}
    return requests.post(
        url="https://api.telegram.org/bot5573262883:AAG3mZAKBS_AcrAeC1doeNnv2AjV4Y4Ecdw/sendMessage",
        json=data,
        headers=headers,
    )


def trigger_active_reminders(*args, **kwargs):
    remind_list = Reminder.objects.filter(
        threshold__lte=timezone.now(),
        reminder_time__lte=timezone.now(),
        is_active=True,
    )
    data = {"chat_id": -1001658596785, "text": "Hi, Alert Fired!"}
    if len(remind_list) == 0:
        return
    for item in remind_list:
        if item.alert_count == 0:
            item.alert_count = 1
            item.save()
            telegram_alert(data=data)
        item.alert_count = 2
        item.is_active = False
        item.save()
        telegram_alert(data=data)
