from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from src.apps.reminders.models import Reminder
from src.utils.fakers import ReminderFactory, UserFactory


class ReminderModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

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
