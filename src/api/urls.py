from django.urls import include, path
from src.api.views.reminders import (
    CreateReminderAPIView,
    GetReminderListAPIView,
    ReminderAPIView,
)

accounts_url_patterns = [
    path(
        "<str:user_id>/reminders/",
        GetReminderListAPIView.as_view(),
        name="reminder_list",
    ),
]

reminders_url_patterns = [
    path(
        "",
        CreateReminderAPIView.as_view(),
        name="create_reminder",
    ),
    path("<str:id>/", ReminderAPIView.as_view(), name="reminder"),
]

V_0_0_0_urlpatterns = [
    path("users/", include(accounts_url_patterns)),
    path("reminders/", include(reminders_url_patterns)),
]

urlpatterns = [
    path("V0.0.0/", include(V_0_0_0_urlpatterns)),
]
