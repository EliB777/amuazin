from pathlib import Path
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

from part_A.reader import Reader
from part_A.metadata import buildMeta
from part_A.convert_to_json import to_json
from part_A.kafka_sub import sendingToKafka
from app.config import AUDIO_DIR, KAFKA_BOOTSTRAP, TOPIC_IN
from app.logger import Logger

# create topic
# def _ensure_topic(bootstrap: str, topic: str, partitions: int = 1, replication: int = 1):
#     admin = KafkaAdminClient(bootstrap_servers=bootstrap)
#     try:
#         admin.create_topics([NewTopic(name=topic, num_partitions=partitions, replication_factor=replication)])
#     except TopicAlreadyExistsError:
#         pass
#     finally:
#         admin.close()
print("hi")
# def main():
logger = Logger.get_logger()
logger.info("started")
print("start")

# using logger if topic already exsist
# try:
#     _ensure_topic(KAFKA_BOOTSTRAP, TOPIC_IN)
#     print("done")
# except Exception as e:
#     logger.error(f"ensure_topic failed: {e}")
#     print("ensure_topic failed")
#     return

folder = Path(AUDIO_DIR)
# folder = r"C:\Users\elibl\podcasts-20250907T074357Z-1-001\podcasts"
paths = Reader().get_path(folder)
# for i in paths:
#     print(i)
builder = buildMeta()
sender = sendingToKafka()


# create metadata end sending + logger
sent = 0
print("1")
for p in paths:
    try:
        meta = builder.build(p)
        logger.info(f"prepared : id={meta['id']} | file={meta['name']} | size={meta['size']} | len_in_sec={meta['len_in_sec']}")
        print(to_json(meta))
        sender.send(meta)
        logger.info(f"send to Kafka | topic={TOPIC_IN} | id={meta['id']}")
        sent += 1
        print(f"sent to Kafka | id={meta['id']}")
    except Exception as e:
        logger.error(f"send to kafka failed | path={p} | err={e}")
        print("sending")

try:
    sender.close()
except Exception as e:
    logger.error(f"kafka close failed: {e}")
print("2")

logger.info(f"finished : sent={sent}")
print("finished")
# folder = Path(AUDIO_DIR)
# paths = Reader().get_path(folder)
# for i in paths:
#     print(i)
# builder = buildMeta()
# sender = sendingToKafka()
print("finished")
