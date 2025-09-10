from elasticsearch import Elasticsearch
from app.config import ES_URL, ES_INDEX

class ESDal:
    def __init__(self):
        self.es = Elasticsearch(ES_URL)

    def get_by_id(self, doc_id):
        return self.es.get(index=ES_INDEX, id=doc_id)

    def search_all(self, size=10):
        return self.es.search(index=ES_INDEX, size=size)

# if __name__ == "_main_":
dal = ESDal()
print("my data")
get = dal.get_by_id("1757514690442")
res = dal.search_all()
for hit in res["hits"]["hits"]:
    print(hit["_id"], hit["_source"])

