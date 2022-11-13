from src.apps.reminders.selectors import (
    get_reminders_by_user_id as get_reminders_by_user_id_selector,
)
from src.apps.reminders.serializers import GetReminderSerializer


def get_reminders_by_user_id(limit=None, offset=None, user_id=None):
    list_reminders = get_reminders_by_user_id_selector(user_id=user_id)
    if not list_reminders:
        return None
    reminders_count = len(list_reminders)
    end = offset + limit
    if end > reminders_count:
        end = reminders_count
    list_reminders = list_reminders[offset:end]
    return GetReminderSerializer(
        list_reminders,
        many=True,
    ).data
