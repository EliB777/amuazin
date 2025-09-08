from pathlib import Path
from pymongo import MongoClient
import gridfs
from app.config import MONGO_HOST, MONGO_PORT, MONGO_DB

class SaveMongoFS:
    def _init_(self):
        self.cli = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.cli[MONGO_DB]
        self.fs = gridfs.GridFS(self.db)

    # seve the file with "gridfs" -> object
    def put(self, enriched: dict):
        p = Path(enriched["path"])
        data = p.read_bytes()
        file_id = self.fs.put(
            data,
            filename=enriched.get("name", p.name),
            metadata=enriched
        )
        return file_id