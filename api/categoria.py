from appwriteClient import db
from appwrite import query
q = query.Query()

def categoria(cat):
    queries = [q.select(["titulo","slug","imagen"]),q.equal('categoria',cat),q.equal("visible",True),q.order_desc('$createdAt')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']
    return docs
