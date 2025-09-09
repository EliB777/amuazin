from part_B.kafka_sub import KafkaIn
from part_B.save_in_mongo import SaveMongoFS
from part_B.save_in_elastic import SaveES
from app.logger import Logger

def main():
    logger = Logger.get_logger()
    logger.info("started and listening")
    print("started and listening")

    consumer = KafkaIn()
    mongo_fs = SaveMongoFS()
    es = SaveES()

    processed = 0
    for idx, msg in enumerate(consumer.stream(), 1):
        try:
            es.index_doc(msg)
            fs_id = mongo_fs.put(msg)
            logger.info(f"[{idx}] stored : id={msg['id']} | file={msg['name']} | fs_id={fs_id}")
            processed += 1
        except Exception as e:
            logger.error(f"[{idx}] persist failed | id={msg.get('id','?')} | file={msg.get('name','?')} | err={e}")

    logger.info(f"finished : processed={processed}")

if __name__ == "_main_":
    main()