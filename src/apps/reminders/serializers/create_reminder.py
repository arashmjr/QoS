from rest_framework import serializers
from src.apps.reminders.models import Reminder


class CreateReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = (
            "title",
            "user",
            "reminder_time",
            "threshold",
        )
