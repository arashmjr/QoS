from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient
from src.utils.fakers import ReminderFactory, UserFactory


class DeleteReminderViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.rc = RequestsClient()
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)

    def make_request(self, headers=None, data=None, id=None):
        return self.rc.delete(
            "http://testserver/api/V0.0.0/reminders/{}/".format(id),
            json=data,
            headers=headers,
        )

    def test_ok_response(self):
        reminder_id = str(self.reminder.id)
        headers = {}
        response = self.make_request(headers=headers, id=reminder_id)
        self.assertEqual(response.status_code, 200)
