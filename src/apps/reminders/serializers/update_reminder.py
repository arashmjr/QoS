from rest_framework import serializers
from src.apps.reminders.models import Reminder


class UpdateReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = (
            "title",
            "message",
            "image",
            "reminder_time",
            "threshold",
            "repeat_interval",
            "alert_count",
            "is_active",
        )
