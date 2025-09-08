from kafka import KafkaProducer
import json
from app.config import KAFKA_BOOTSTRAP, TOPIC_IN

# create Producer and sending to kafka
class sendingToKafka:
    def _init_(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, data: dict):
        self.producer.send(TOPIC_IN, data)
        self.producer.flush()

    def close(self):
        self.producer.close()