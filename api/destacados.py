from appwriteClient import db
from appwrite import query
q = query.Query()

def destacados():
    queries = [q.equal('visible',True),q.equal('es_destacado',True),q.order_desc('fecha')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']    
    return docs