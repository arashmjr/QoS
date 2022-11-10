from rest_framework import serializers
from src.apps.reminders.models import Reminder
from src.apps.storage.services import serialize_media_by_id


class GetReminderSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reminder
        fields = (
            "id",
            "title",
            "message",
            "image",
            "reminder_time",
            "threshold",
            "repeat_interval",
            "created_at",
            "updated_at",
        )

    def get_image(self, obj):
        if obj.image is None:
            return None
        return serialize_media_by_id(media_id=obj.image_id)
