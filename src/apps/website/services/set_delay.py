from src.apps.website.models import Website


def set_delay(delay, address):
    
    return Website.objects.filter(address=address).update(delay=delay)
