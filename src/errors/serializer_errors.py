class SerializerErrors:
    class CreateReminderSerializer:
        errors = {
            "user": "CREATE_REMINDER_SERIALIZER_INVALID_USER",
            "reminder_time": "CREATE_REMINDER_SERIALIZER_INVALID_REMINDER_TIME",
            "threshold": "CREATE_REMINDER_SERIALIZER_INVALID_THRESHOLD",
        }
