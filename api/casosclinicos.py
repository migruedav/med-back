from appwriteClient import db
from appwrite import query

q = query.Query()


def casosclinicos():
    queries = [
        q.select(["titulo", "imagen", "fecha", "autor", "slug"]),
        q.equal("visible", True),
        q.equal("categoria", "Casos Clínicos"),
        q.order_desc("fecha"),
    ]
    data = db.list_documents("med-cmc", "posts", queries=queries)
    docs = data["documents"]
    return docs
