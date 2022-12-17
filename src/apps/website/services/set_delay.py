from src.apps.website.models import Website


def set_delay(delay, address):
    Website.objects.filter(address=address).update(delay=delay)
