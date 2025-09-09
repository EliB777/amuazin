from elasticsearch import Elasticsearch
from app.config import ES_URL, ES_INDEX

# create index
class SaveES:
    def _init_(self):
        self.es = Elasticsearch(ES_URL)
        if not self.es.indices.exists(index=ES_INDEX):
            self.es.indices.create(index=ES_INDEX)

    def index_doc(self, body: dict):
        self.es.index(index=ES_INDEX, id=body.get("id"), document=body)