from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.reminders.services import get_reminders_by_user_id
from src.errors import BadRequestException, ErrorEnum, NotFoundException


class GetReminderListAPIView(APIView):
    def get(self, *args, **kwargs):
        user_id = kwargs.get("user_id")
        limit = self.request.query_params.get("limit", "10")
        offset = self.request.query_params.get("offset", "0")
        try:
            limit = int(limit)
            offset = int(offset)
        except Exception:
            raise BadRequestException(
                message={"Reminder": _("limit and offset is not valid")},
                error_type=[ErrorEnum.Reminder.INVALID_LIMIT_AND_OFFSET],
            )
        data = get_reminders_by_user_id(
            limit=limit, offset=offset, user_id=user_id
        )
        if data is None:
            raise NotFoundException(
                message={"user_id": _("No such reminder for this user")},
                error_type=[ErrorEnum.Service.INVALID_USER_ID],
            )
        return Response(
            data={"ok": True, "data": data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
