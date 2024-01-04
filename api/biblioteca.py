from appwriteClient import db
from appwrite import query
q = query.Query()

def biblioteca():
    queries = [q.select(['titulo',"imagen", "titulo", "fecha", "autor", "slug"]),q.equal('visible',True),q.equal('categoria','Biblioteca Clínica'),q.order_desc('fecha')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']    
    return docs