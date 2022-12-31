from core.celery_conf import app_celery
from src.utils.rabbitmq import receiver, sender


@app_celery.task(name="test_sites_delay")
def test_async_sites_delay_task(web_urls: list):
    sender(web_urls=web_urls)
    # if you are on server set host to ip address
    receiver(host="localhost", count_obj=len(web_urls))
