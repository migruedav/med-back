from appwriteClient import db
from appwrite import query
q = query.Query()

def examenes(offset):
    queries = [q.offset(100*offset), q.limit(100),q.sort('$createdAt')]
    data = db.list_documents('med-cmc','examenes',queries=queries)
    docs = data['documents']
    return docs
