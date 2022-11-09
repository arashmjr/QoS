from rest_framework import serializers
from src.apps.reminders.models import Reminder


class CreateReminderSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reminder
        fields = (
            "title",
            "user",
            "message",
            "image",
            "reminder_time",
            "threshold",
            "repeat_interval",
            "created_at",
            "upadted_at",
        )
