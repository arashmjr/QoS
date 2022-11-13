from src.apps.reminders.models import Reminder


def get_reminders_by_user_id(user_id):
    return Reminder.objects.filter(user__id=user_id).order_by("-created_at")
