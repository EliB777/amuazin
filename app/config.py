from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJECT_ROOT / "data" / "podcasts"
# AUDIO_DIR =r"C:\Users\elibl\podcasts-20250907T074357Z-1-001\podcasts"

# Kafka
KAFKA_BOOTSTRAP = "localhost:9092"
TOPIC_IN = "audio_filee"

# MongoDB
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB   = "ExamDB"

# Elasticsearch
ES_URL   = "http://localhost:9200"
ES_INDEX = "audio_files_index"

# Logger
LOG_NAME  = "audio_pipeline"
LOG_INDEX = "pipeline_logs"

# # Clasifier
THRESHOLD = 1.0
MEDIUM_MIN = 1.0
HIGH_MIN   = 3.0
# or
MIN_HITS_MEDIUM = 3
MIN_HITS_HIGH   = 6

# lists for decode
HOSTILE = ("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUs"
    "TmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMs"
    "QmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
LESS_HOSTILE = (
"RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZ"
    "SBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
)

# testing

# BDS_THRESHOLD = 1.0
# BDS_MEDIUM_MIN = 1.0
# BDS_HIGH_MIN   = 3.0
#
# BDS_MIN_HITS_MEDIUM = 3
# BDS_MIN_HITS_HIGH   = 6