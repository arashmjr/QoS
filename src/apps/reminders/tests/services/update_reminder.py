from decimal import Decimal

from django.test import TestCase
from src.apps.reminders.services import update_reminder
from src.errors import BadRequestException
from src.utils.fakers import ReminderFactory, UserFactory


class UpdateReminderServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)
        self.updated_reminder = ReminderFactory(user=self.user)

    def test_update_reminder_service(self):
        invalid_data = {
            "title": False,
            "message": False,
            "reminder_time": "invalid",
            "threshold": "invalid",
        }
        with self.assertRaises(BadRequestException):
            update_reminder(
                reminder_id=self.reminder.id,
                data=invalid_data,
            )

        valid_data = {
            "title": "valid",
            "message": "sample text",
            "reminder_time": self.updated_reminder.reminder_time,
            "threshold": self.updated_reminder.threshold,
        }
        update_reminder(
            reminder_id=self.reminder.id,
            data=valid_data,
        )
        self.reminder.refresh_from_db()
        self.assertEqual(
            self.reminder.title,
            valid_data.get("title"),
        )
        self.assertEqual(
            self.reminder.message,
            valid_data.get("message"),
        )
        self.assertEqual(
            self.reminder.reminder_time,
            valid_data.get("reminder_time"),
        )
        self.assertEqual(
            self.reminder.threshold,
            valid_data.get("threshold"),
        )
