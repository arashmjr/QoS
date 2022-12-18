import pika


def sender(web_urls):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="185.130.78.42")
    )
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)

    for item in web_urls:
        channel.basic_publish(
            exchange="",
            routing_key="task_queue",
            body=item.address,
        )
        print("message send")

    connection.close()
