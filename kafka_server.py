import producer_server


def run_kafka_server():
    input_file = "./police-department-calls-for-service.json"

    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="com.udacity.police.calls",
        bootstrap_servers="localhost:9092",
        api_version=(0, 10, 1), #looks like i need this to get rid of NoBrokersAvailable error
        client_id="hm" 
    )
    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
