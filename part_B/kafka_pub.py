from kafka import KafkaConsumer
import json
from app.config import KAFKA_BOOTSTRAP, TOPIC_IN

class KafkaIn:
    def __init__(self):
        self.c = KafkaConsumer(
            TOPIC_IN,
            bootstrap_servers=KAFKA_BOOTSTRAP,
            # auto_offset_reset="earliest",
            # enable_auto_commit=True,
            value_deserializer=lambda b: json.loads(b.decode("utf-8"))
        )
    def stream(self):
        for m in self.c:
            yield m.value