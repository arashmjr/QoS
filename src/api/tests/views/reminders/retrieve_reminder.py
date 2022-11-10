from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient
from src.apps.reminders.services import get_reminder_by_id
from src.utils.fakers import ReminderFactory, UserFactory


class RetrieveReminderViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.rc = RequestsClient()
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)

    def make_request(self, data=None, id=None):
        return self.rc.get(
            "http://testserver/api/V0.0.0/reminders/{}/".format(id),
            json=data,
        )

    def test_ok_response(self):
        reminder_id = str(self.reminder.id)
        response = self.make_request(id=reminder_id)
        self.assertEqual(response.status_code, 200)
        reminder = get_reminder_by_id(reminder_id)
        self.assertEqual(reminder, response.json().get("data").get("reminder"))
