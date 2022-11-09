from src.apps.storage.selectors import get_media_by_id
from src.apps.storage.serializers import MediaModelSerializer


def serialize_media_by_id(media_id):
    media = get_media_by_id(media_id=media_id)
    serializer = MediaModelSerializer(media)
    serializer_data = serializer.data
    return serializer_data
