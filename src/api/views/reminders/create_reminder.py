from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.reminders.services import create_reminder
from src.errors.exceptions import BadRequestException


class CreateReminderAPIView(APIView):
    def post(self, request):
        done, errs, reminder = create_reminder(data=self.request.data)
        if not done:
            raise BadRequestException(
                message=errs.get("errors"),
                error_type=errs.get("error_type"),
            )
        data = {"reminder": reminder}
        return Response(
            data={
                "ok": True,
                "data": data,
                "status": status.HTTP_201_CREATED,
            },
            status=status.HTTP_201_CREATED,
        )
