from django.db import transaction
from src.apps.reminders.serializers import (
    CreateReminderSerializer,
    GetReminderSerializer,
)
from src.errors import SerializerErrors


@transaction.atomic
def create_reminder(data):
    errs = {}
    done = False
    reminder = None
    error_dict = SerializerErrors.CreateReminderSerializer.errors
    serializer = CreateReminderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        done = True
        reminder = GetReminderSerializer(serializer.instance, many=False).data
    else:
        error_types = []
        errors = serializer.errors
        for error in errors.keys():
            error_type = error_dict.get(error)
            error_types.append(error_type)
        errs["erros"] = errors
        errs["error_type"] = error_types
    return (done, errs, reminder)
