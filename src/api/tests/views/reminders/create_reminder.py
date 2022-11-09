import json
from datetime import timedelta

from django.test import LiveServerTestCase
from django.utils import timezone
from rest_framework.test import RequestsClient
from src.errors import SerializerErrors
from src.utils.fakers import UserFactory


class CreateReminderAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.rc = RequestsClient()
        self.user = UserFactory()

    def make_request(self, data=None):
        return self.rc.post(
            "http://testserver/api/V0.0.0/reminders/create-reminder/",
            json=data,
        )

    def test_bad_request_response(self):
        def post_bad_request(error_type, data=None):
            response = self.make_request(data=data)
            self.assertEqual(response.status_code, 400)
            error_set = set(error_type)
            data_error = response.json().get("error_type")
            data_error_set = set(data_error)
            self.assertSetEqual(
                error_set,
                data_error_set,
            )

        post_bad_request(
            error_type=[
                SerializerErrors.CreateReminderSerializer.errors.get("user"),
                SerializerErrors.CreateReminderSerializer.errors.get(
                    "reminder_time"
                ),
                SerializerErrors.CreateReminderSerializer.errors.get(
                    "threshold"
                ),
            ],
            data={
                "user": None,
                "reminder_time": "invalid",
                "threshold": "invalid",
            },
        )

    def test_created_response(self):
        data = {
            "title": "test",
            "user": str(self.user.id),
            "reminder_time": json.dumps(
                timezone.now() + timedelta(days=5),
                default=str,
            ),
            "threshold": json.dumps(
                timezone.now() + timedelta(days=3),
                default=str,
            ),
        }

        response = self.make_request(data=data)
        self.assertEqual(response.status_code, 201)
