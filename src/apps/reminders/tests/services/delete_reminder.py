from django.test import TestCase
from src.apps.reminders.models import Reminder
from src.apps.reminders.services import delete_reminder, get_reminder_by_id
from src.utils.fakers import ReminderFactory, UserFactory


class DeleteReminderServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)

    def test_delete_reminder_service(self):
        delete_reminder(self.reminder.id)
        with self.assertRaises(Reminder.DoesNotExist):
            get_reminder_by_id(self.reminder.id)
