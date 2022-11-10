import json

from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient
from src.apps.reminders.services import get_reminder_by_id
from src.errors import SerializerErrors
from src.utils.fakers import ReminderFactory, UserFactory


class UpdateReminderViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.rc = RequestsClient()
        self.user = UserFactory()
        self.reminder = ReminderFactory(user=self.user)
        self.updated_reminder = ReminderFactory(user=self.user)

    def make_request(self, headers=None, data=None, id=None):
        return self.rc.patch(
            "http://testserver/api/V0.0.0/reminders/{}/".format(id),
            json=data,
            headers=headers,
        )

    def test_bad_request_response(self):
        def post_bad_request(error_type, data=None, headers=None, id=None):
            response = self.make_request(data=data, headers=headers, id=id)

            self.assertEqual(response.status_code, 400)
            error_set = set(error_type)
            data_error = response.json().get("error_type")
            data_error_set = set(data_error)
            self.assertSetEqual(
                error_set,
                data_error_set,
            )

        invalid_data = {
            "title": False,
            "message": False,
            "reminder_time": "invalid",
            "threshold": "invalid",
        }

        reminder_id = str(self.reminder.id)
        post_bad_request(
            SerializerErrors.UpdateReminderSerializer.errors.values(),
            headers={},
            data=invalid_data,
            id=reminder_id,
        )

    def test_ok_response(self):
        valid_data = {
            "title": "valid",
            "message": "sample text",
            "reminder_time": json.dumps(
                self.updated_reminder.reminder_time,
                default=str,
            ),
            "threshold": json.dumps(
                self.updated_reminder.threshold,
                default=str,
            ),
        }
        headers = {}
        reminder_id = str(self.reminder.id)
        response = self.make_request(
            data=valid_data, headers=headers, id=reminder_id
        )
        self.reminder.refresh_from_db()
        reminder = get_reminder_by_id(reminder_id)
        self.assertEqual(reminder, response.json().get("data").get("reminder"))
        self.assertEqual(response.status_code, 200)
