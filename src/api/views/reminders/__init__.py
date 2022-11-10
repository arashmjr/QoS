from src.api.views.reminders.create_reminder import CreateReminderAPIView
from src.api.views.reminders.retrieve_reminder import RetrieveReminderAPIView
from src.api.views.reminders.update_reminder import UpdateReminderAPIView


class ReminderAPIView(RetrieveReminderAPIView, UpdateReminderAPIView):
    pass
