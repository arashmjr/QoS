from src.apps.reminders.selectors import (
    get_reminder_by_id as get_reminder_by_id_selector,
)
from src.apps.reminders.serializers import GetReminderSerializer


def get_reminder_by_id(reminder_id):
    reminder = get_reminder_by_id_selector(reminder_id=reminder_id)
    serializer = GetReminderSerializer(reminder)
    data = serializer.data
    return data
