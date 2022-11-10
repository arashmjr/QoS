from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from src.apps.reminders.models import Reminder
from src.utils.fakers import ReminderFactory, UserFactory


class ReminderModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)

    def test_clean_method(self):
        with self.assertRaises(ValidationError):
            ReminderFactory(
                reminder_time=timezone.now() - timedelta(days=5),
                threshold=timezone.now() + timedelta(minutes=5),
            )
        with self.assertRaises(ValidationError):
            ReminderFactory(
                reminder_time=timezone.now() + timedelta(days=5),
                threshold=timezone.now() + timedelta(days=10),
            )
        with self.assertRaises(ValidationError):
            ReminderFactory(
                reminder_time=timezone.now() + timedelta(days=5),
                threshold=timezone.now() - timedelta(days=5),
            )

    def test_reminder_str_method(self):

        reminder_string_object = str(self.reminder)
        expecting_data = self.reminder.title
        self.assertEqual(reminder_string_object, expecting_data)
