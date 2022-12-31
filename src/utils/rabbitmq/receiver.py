import sys

import pika
from src.apps.website.services import calculate_delay_service


def receiver(host, count_obj):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    ch2 = connection.channel()
    ch2.queue_declare(queue="task_queue", durable=True)
    print("waiting for message, to exit ctrl+c")

    def callback(ch, method, properties, body):
        calculate_delay_service(host=body.decode())

        if method.delivery_tag == count_obj:
            # sys.exit()
            ch2.close()
            return

    ch2.basic_qos(prefetch_count=1)
    ch2.basic_consume(
        queue="task_queue", on_message_callback=callback, auto_ack=True
    )

    ch2.start_consuming()
