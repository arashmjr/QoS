from django.urls import include, path
from src.api.views.reminders import (
    CreateReminderAPIView,
    UpdateReminderAPIView,
)

reminders_url_patterns = [
    path(
        "create-reminder/",
        CreateReminderAPIView.as_view(),
        name="create_reminder",
    ),
    path("<str:id>/", UpdateReminderAPIView.as_view(), name="reminders"),
]

V_0_0_0_urlpatterns = [
    path("reminders/", include(reminders_url_patterns)),
]

urlpatterns = [
    path("V0.0.0/", include(V_0_0_0_urlpatterns)),
]
