import sys

import pika
import requests


def receiver(host, count_obj):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    ch2 = connection.channel()
    ch2.queue_declare(queue="task_queue", durable=True)
    print("waiting for message, to exit ctrl+c")

    def callback(ch, method, properties, body):

        url = "http://localhost:8000/api/V0.0.0/website/calculate-delay/"
        headers = {"Content-type": "application/json"}
        response = requests.put(
            url=url,
            json=body.decode(),
            headers=headers,
        )
        if method.delivery_tag == count_obj:
            sys.exit()

    ch2.basic_qos(prefetch_count=1)
    ch2.basic_consume(
        queue="task_queue", on_message_callback=callback, auto_ack=True
    )

    ch2.start_consuming()
