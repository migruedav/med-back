from appwriteClient import db
from appwrite import query
q = query.Query()

def ads(position):
    queries = [q.equal('visible',True),q.order_desc('$createdAt')]
    data = db.list_documents('med-cmc','ads',queries=queries)
    docs = data['documents']
    docs = [x for x in docs if position in x['visible_en']]  
    return docs

