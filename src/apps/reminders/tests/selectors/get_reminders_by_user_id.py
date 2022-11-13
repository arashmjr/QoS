from django.test import TestCase
from src.apps.reminders.selectors import get_reminders_by_user_id
from src.utils.fakers import ReminderFactory, UserFactory


class GetRemindersByUserIdSelectorsTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.reminders = ReminderFactory.create_batch(size=5, user=self.user)

    def test_get_reminders_by_user_id_selector(self):
        reminders = get_reminders_by_user_id(user_id=self.user.id)
        self.assertEqual(len(reminders), 5)
