from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.reminders.services import get_reminder_by_id


class RetrieveReminderAPIView(APIView):
    def get(self, *args, **kwargs):
        reminder_id = kwargs.get("id")
        reminder = get_reminder_by_id(reminder_id=reminder_id)
        return Response(
            data={
                "ok": True,
                "data": {"reminder": reminder},
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )
