from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.apps.website.services import upload_csv_service


class UploadFileAPIView(APIView):
    def post(self, *args, **kwargs):
        csv_file = self.request.FILES["csv_file"]
        file_name_suffix = csv_file.name.split(".")[-1]
        if file_name_suffix not in [
            "csv",
        ]:
            return Response({"message": "Wrong file format"})
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        upload_csv_service(csv_data)
        return Response(
            data={
                "ok": True,
                "data": None,
                "status": status.HTTP_201_CREATED,
            },
            status=status.HTTP_201_CREATED,
        )
