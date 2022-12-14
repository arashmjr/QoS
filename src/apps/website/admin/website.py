from django.contrib import admin
from src.apps.website.models import Website


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass
