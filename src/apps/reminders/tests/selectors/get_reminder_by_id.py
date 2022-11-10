from django.test import TestCase
from src.apps.reminders.selectors import get_reminder_by_id
from src.utils.fakers import ReminderFactory


class GetReminderSelectorTestCase(TestCase):
    def setUp(self):
        self.reminder = ReminderFactory()

    def test_get_reminder_by_id_selector(self):

        reminder = get_reminder_by_id(reminder_id=self.reminder.id)
        self.assertEqual(reminder, self.reminder)
