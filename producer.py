from confluent_kafka import Producer
from typing import Any, Dict
import json
import uuid

# Setup
producer_config: Dict[str, Any] = {"bootstrap.servers": "localhost:9092"}
producer = Producer(producer_config)


# --- Example Usage ---
def delivery_report(err, _):
    if err:
        print("❌")
    else:
        print("✅")


example_order = {
    "order_id": str(uuid.uuid4()),
    "user": "david",
    "item": "computer",
    "quantity": 1,
}

value = json.dumps(example_order).encode("utf-8")
producer.produce(topic="orders", value=value, callback=delivery_report)
producer.flush()  # Safe termination
