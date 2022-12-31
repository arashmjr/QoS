from django.urls import include, path
from src.api.views.website import TestDelayAPIView, UploadFileAPIView

website_url_patterns = [
    path("upload-csv/", UploadFileAPIView.as_view(), name="upload_csv"),
    path(
        "test-delay/",
        TestDelayAPIView.as_view(),
        name="test_delay",
    ),
]

V_0_0_0_urlpatterns = [
    path("website/", include(website_url_patterns)),
]

urlpatterns = [
    path("V0.0.0/", include(V_0_0_0_urlpatterns)),
]
