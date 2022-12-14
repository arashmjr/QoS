from src.apps.website.selectors import create_csv_item_selector


def upload_csv_service(csv_data: list):
    for item in csv_data:
        address = item.split(",")
        if address[0] != "" and address[0] != "address":
            create_csv_item_selector(address[0])
