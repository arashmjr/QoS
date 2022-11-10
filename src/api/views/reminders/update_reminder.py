from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.reminders.services import update_reminder


class UpdateReminderAPIView(APIView):
    def patch(self, *args, **kwargs):
        reminder_id = kwargs.get("id")
        new_reminder = update_reminder(
            reminder_id=reminder_id, data=self.request.data
        )
        return Response(
            data={
                "ok": True,
                "data": {"reminder": new_reminder},
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )
