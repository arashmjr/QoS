from django.test import TestCase
from src.apps.reminders.serializers import GetReminderSerializer
from src.apps.reminders.services import get_reminder_by_id
from src.utils.fakers import ReminderFactory, UserFactory


class GetReminderByIdServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)

    def test_get_reminder_by_id_service(self):
        data = get_reminder_by_id(reminder_id=self.reminder.id)
        expected_data = GetReminderSerializer(self.reminder).data
        self.assertDictEqual(expected_data, data)
