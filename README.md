
# kafka_tools
Package contains helpers to consume and produce with Kafka.
  


**Installation**

    pip install git+https://github.com/nops-io/kafka_tools.git@master

**Usage**:

Producing and consuming. `Consumer` returns iterator.

    from kafka_tools import Producer, Consumer

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
