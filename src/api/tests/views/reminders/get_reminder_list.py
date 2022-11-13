import uuid
from urllib.parse import urlencode

from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient
from src.errors import ErrorEnum
from src.utils.fakers import ReminderFactory, UserFactory


class GetReminderListAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.rc = RequestsClient()
        self.user = UserFactory()
        self.reminders = ReminderFactory.create_batch(5, user=self.user)

    def make_request(
        self, limit=None, offset=None, user_id=None, headers=None
    ):
        query = {}
        if limit is not None:
            query["limit"] = limit
        if offset is not None:
            query["offset"] = offset
        url = "http://testserver/api/V0.0.0/users/{}/reminders/".format(
            user_id
        )
        if len(query) != 0:
            query_string = urlencode(query)
            url = "{}?{}".format(url, query_string)
        return self.rc.get(url, headers=headers)

    def test_badrequest_response(self):
        response = self.make_request(limit="invalid", headers={})
        error_type = response.json().get("error_type")
        self.assertListEqual(
            error_type, [ErrorEnum.Reminder.INVALID_LIMIT_AND_OFFSET]
        )
        self.assertEqual(response.status_code, 400)

    def test_notfound_response(self):
        response = self.make_request(headers={}, id=str(uuid.uuid4()))
        self.assertEqual(response.status_code, 404)
        error = response.json().get("error_type")
        self.assertListEqual(error, [ErrorEnum.Service.INVALID_USER_ID])

    def test_ok_response(self):
        response = self.make_request(headers={}, user_id=self.user.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("ok"), True)
        self.assertEqual(response.json().get("status"), 200)
