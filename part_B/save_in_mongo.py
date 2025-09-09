from pathlib import Path
from pymongo import MongoClient
import gridfs
from app.config import MONGO_HOST, MONGO_PORT, MONGO_DB

class SaveMongoFS:
    def _init_(self):
        self.cli = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.cli[MONGO_DB]
        self.fs = gridfs.GridFS(self.db)

    # seve the file with "gridfs" + metadata
    def put(self, metadata: dict):
        p = Path(metadata["path"])
        data = p.read_bytes()
        return self.fs.put(
            data,
            # id = metadata["id"],
            # filename=metadata["name"],
            metadata=metadata
        )
