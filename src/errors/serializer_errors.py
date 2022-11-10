class SerializerErrors:
    class CreateReminderSerializer:
        errors = {
            "title": "CREATE_REMINDER_SERIALIZER_INVALID_TITLE",
            "user": "CREATE_REMINDER_SERIALIZER_INVALID_USER",
            "message": "CREATE_REMINDER_SERIALIZER_INVALID_MESSAGE",
            "reminder_time": "CREATE_REMINDER_SERIALIZER_INVALID_REMINDER_TIME",
            "threshold": "CREATE_REMINDER_SERIALIZER_INVALID_THRESHOLD",
        }

    class UpdateReminderSerializer:
        errors = {
            "title": "UPDATE_REMINDER_SERIALIZER_INVALID_TITLE",
            "message": "UPDATE_REMINDER_SERIALIZER_INVALID_MESSAGE",
            "reminder_time": "UPDATE_REMINDER_SERIALIZER_INVALID_REMINDER_TIME",
            "threshold": "UPDATE_REMINDER_SERIALIZER_INVALID_THRESHOLD",
        }
