from django.contrib import admin
from src.apps.reminders.models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    pass
