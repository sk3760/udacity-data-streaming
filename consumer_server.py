import asyncio
from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient


BROKER_URL = "localhost:9092"

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])
    #print(f"Topic name: {topic_name}")
    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
             print(f'message: {message.value()}')
        await asyncio.sleep(1.0)


def main():
    """Checks for topic and creates the topic if it does not exist"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})

    try:
        asyncio.run(consume("com.udacity.police.calls"))
    except KeyboardInterrupt as e:
        print("shutting down")

if __name__ == "__main__":
    main()
    


