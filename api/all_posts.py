from appwriteClient import db
from appwrite import query
q = query.Query()

def all_posts(offset):

    queries = [q.offset(100*offset), q.limit(100), q.equal('visible',True),q.order_desc('fecha')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']

    return {"len": len(docs), "posts": docs}
        