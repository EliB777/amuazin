from part_B.kafka_pub import KafkaIn
from part_B.save_in_mongo import SaveMongoFS
from part_B.save_in_elastic import SaveES
from app.logger import Logger
from part_B.audio_to_text import Transcriber


def main():
    logger = Logger.get_logger()
    logger.info("started and listening")

    consumer = KafkaIn()
    mongo_fs = SaveMongoFS()
    es = SaveES()
    asr = Transcriber(lang="en-US")

    processed = 0
    for idx, msg in enumerate(consumer.stream(), 1):
        try:
            msg["transcript"] = asr.transcribe(msg["file_path"])
            es.index_doc(msg)
            fs_id = mongo_fs.put(msg)

            logger.info(f"[{idx}] stored : id={msg['id']} | file={msg['file_name']} | fs_id={fs_id} | transcript_len={len(msg['transcript'])}")
            processed += 1
        except Exception as e:
            logger.error(f"[{idx}] persist failed : id={msg.get('id','?')} | file={msg.get('file_name','?')} | err={e}")

    logger.info(f"finished : processed={processed}")

if __name__ == "_main_":
    main()