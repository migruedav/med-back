from appwriteClient import db
from appwrite.query import Query

q = Query()

def posts_to_edit(orderedby,offset):

    queries = [q.select(["titulo","fecha","slug","visible"]),q.offset(20*offset), q.limit(20), q.order_desc(orderedby)]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']

    return docs
        