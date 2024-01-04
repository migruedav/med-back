from appwriteClient import db
from appwrite import query
q = query.Query()

def especialidad_related(esp):
    queries = [q.equal('especialidad_principal',esp),q.equal("visible",True),q.limit(6),q.order_desc('$createdAt')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']
    return docs
