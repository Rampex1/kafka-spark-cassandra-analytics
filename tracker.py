from confluent_kafka import Consumer
from typing import Any
import json

# Setup
consumer_config: dict[str, Any] = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(consumer_config)
consumer.subscribe(["example_topic"])
print("Consumer is running")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue
        else:
            value = msg.value()
            if value is None:
                continue
            value.decode("utf-8")

            # --- Example message handling ---
            order = json.loads(value)
            print(
                f"Received order: {order['quantity']} x {order['item']} from {order['user']}"
            )

except KeyboardInterrupt:
    print("\n 🔴 Stopping consumer")

finally:
    consumer.close()
