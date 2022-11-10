import uuid
from typing import Union

from src.apps.reminders.models import Reminder


def delete_reminder(reminder_id: Union[str, uuid.UUID]):
    Reminder.objects.filter(id=reminder_id).delete()
