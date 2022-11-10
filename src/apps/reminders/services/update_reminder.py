from src.apps.reminders.selectors import get_reminder_by_id
from src.apps.reminders.serializers import UpdateReminderSerializer
from src.apps.reminders.services import (
    get_reminder_by_id as get_reminder_by_id_service,
)
from src.errors import BadRequestException, SerializerErrors


def update_reminder(reminder_id, data):
    reminder = get_reminder_by_id(reminder_id=reminder_id)
    serializer = UpdateReminderSerializer(
        instance=reminder,
        data=data,
        partial=True,
    )
    if serializer.is_valid():
        serializer.save()
        return get_reminder_by_id_service(reminder_id=reminder_id)
    errors = serializer.errors
    error_types = []
    for error in errors.keys():
        error_type = SerializerErrors.UpdateReminderSerializer.errors.get(
            error
        )
        error_types.append(error_type)
    raise BadRequestException(message=errors, error_type=error_types)
