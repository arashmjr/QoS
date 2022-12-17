from src.apps.website.models import Website


def get_list_urls():
    return Website.objects.all()
