from appwriteClient import db
from appwrite import query
q = query.Query()

def all_posts():
    all_posts = []
    for i in range(5):
        queries = [q.offset(100*i), q.limit(100), q.equal('visible',True),q.order_desc('fecha')]
        data = db.list_documents('med-cmc','posts',queries=queries)
        docs = data['documents']
        all_posts.append(docs)

    return all_posts 
        