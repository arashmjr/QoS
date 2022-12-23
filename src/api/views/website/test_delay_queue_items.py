from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.website.services import get_list_urls
from src.utils.rabbitmq import receiver, sender


class TestDelayFromQueueItems(APIView):
    def get(self, *args, **kwargs):
        web_urls = get_list_urls()
        sender(web_urls=web_urls)
        try:
            receiver(host="localhost", count_obj=len(web_urls))
        except:
            return Response(
                data={
                    "ok": True,
                    "data": None,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
