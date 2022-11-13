import uuid

from django.test import TestCase
from src.apps.reminders.serializers import GetReminderSerializer
from src.apps.reminders.services import get_reminders_by_user_id
from src.utils.fakers import ReminderFactory, UserFactory


class GetRemindersByUserIdServicesTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminders = ReminderFactory.create_batch(size=5, user=self.user)
        self.reminders.sort(key=lambda x: x.created_at, reverse=True)

    def test_get_reminders_by_user_id_services(self):
        data = get_reminders_by_user_id(
            limit=10, offset=0, user_id=self.user.id
        )
        expected_data = GetReminderSerializer(self.reminders, many=True).data
        self.assertEqual(data, expected_data)

    def test_get_reminders_by_invalid_user_id(self):
        reminders = get_reminders_by_user_id(
            limit=10, offset=0, user_id=str(uuid.uuid4())
        )
        self.assertIsNone(reminders)
