
# nops-kafka
Package contains helpers to consume and produce using Kafka.
  


**Installation**

    pip install nops-kafka

**Usage**:

Producing and consuming. `Consumer` returns iterator.

    from nops_kafka import Producer, Consumer

    bootstrap_servers = "kafka.kafka.svc.cluster.local:9092"

    producer = Producer(bootstrap_servers=bootstrap_servers)
    producer.send("topicname", value={"any": "payload"}, headers={"and": "any_headers"})
    producer.flush()

    # For consuming single or multiple topics at once
    consumer = Consumer(bootstrap_servers=bootstrap_servers, group_id="KAFKA_CONSUMER_GROUP_ID", auto_offset_reset="latest")
    consumer.subscribe(["topicname"])

    event = next(consumer.receive())
    print(event)

    for event in consumer.receive():
        yield event
