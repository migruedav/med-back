from appwriteClient import db
from appwrite import query
q = query.Query()

def heroslider():
    queries = [q.select(['titulo',"imagen", "autor", "slug"]),q.equal('hero_slider',True),q.order_desc('fecha')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']    
    return docs
