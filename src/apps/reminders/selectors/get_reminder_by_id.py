import uuid
from typing import Union

from src.apps.reminders.models import Reminder


def get_reminder_by_id(reminder_id: Union[str, uuid.UUID]):
    return Reminder.objects.get(id=reminder_id)
