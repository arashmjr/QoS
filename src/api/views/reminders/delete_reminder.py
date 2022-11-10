from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.reminders.services import delete_reminder


class DeleteReminderAPIView(APIView):
    def delete(self, *args, **kwargs):
        reminder_id = kwargs.get("id")
        delete_reminder(reminder_id=reminder_id)
        return Response(
            data={"ok": True, "data": {}, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
