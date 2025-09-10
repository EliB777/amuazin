from part_B.kafka_pub import KafkaIn
from part_B.save_in_mongo import SaveMongoFS
from part_B.save_in_elastic import SaveES
from part_B.audio_to_text import Transcriber
from app.logger import Logger
from part_B.clasifier_and_enricher import enrich

# def main():
logger = Logger.get_logger()
logger.info("started and listening")

consumer = KafkaIn()
mongo_fs = SaveMongoFS()
es = SaveES()
asr = Transcriber(lang="en-US")
# תמלול + חישוב מסוכנות
processed = 0
for idx, msg in enumerate(consumer.stream(), 1):
    try:
        msg["transcript"] = asr.transcribe(msg["path"])
        msg = enrich(msg, transcript_field="transcript")
        es.index_doc(msg)
        fs_id = mongo_fs.put(msg)
        logger.info(
            f"[{idx}] stored : id={msg['id']} | file={msg['name']} "
            f"| fs_id={fs_id} | transcript_len={len(msg['transcript'])} "
            f"| bds={msg['is_bds']} | level={msg['bds_threat_level']} | pct={msg['bds_percent']}"
        )
        processed += 1
    except Exception as e:
        logger.error(
            f"[{idx}] persist failed : id={msg.get('id','?')} | file={msg.get('name','?')} | err={e}"
        )

logger.info(f"finished : processed={processed}")
print("finished")
# if __name__ == "_main_":
#     main()