from appwriteClient import db
from appwrite.query import Query

q = Query()

def posts_to_edit(offset):

    queries = [q.offset(20*offset), q.limit(20), q.equal('visible',True),q.order_desc('fecha')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']

    return docs
        