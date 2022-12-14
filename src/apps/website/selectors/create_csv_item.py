from src.apps.website.models import Website


def create_csv_item_selector(address: str):
    Website.objects.create(address=address)
