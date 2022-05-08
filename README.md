
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

    consumer = Consumer("topicname", bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
    event = next(consumer.receive())
    print(event)
