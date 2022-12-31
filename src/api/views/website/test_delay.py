from threading import Thread

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.website.services import get_list_urls
from src.apps.website.tasks import test_async_sites_delay_task


class TestDelayAPIView(APIView):
    def get(self, *args, **kwargs):
        web_urls = get_list_urls()

        test_async_sites_delay_task.delay(web_urls=web_urls)
        return Response(
            data={
                "ok": True,
                "data": None,
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )
