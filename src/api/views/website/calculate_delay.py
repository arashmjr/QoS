import subprocess
from time import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.website.services import set_delay


class CalculateDelayAPIView(APIView):
    def put(self, *args, **kwargs):
        host = self.request.data
        ping = subprocess.Popen(
            ["ping", "-c", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time_before = time()
        out = ping.communicate()
        time_after = time()
        delay = time_after - time_before

        set_delay(address=host, delay=delay)
        return Response(
            data={
                "ok": True,
                "data": None,
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )
