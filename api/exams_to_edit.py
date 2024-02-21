from appwriteClient import db
from appwrite.query import Query

q = Query()

def exams_to_edit(offset,orderedby):

    if orderedby == "fecha":
        queries = [q.offset(20*offset),q.limit(20), q.order_desc(orderedby)]
    else:
        queries = [q.offset(20*offset),q.limit(20), q.order_asc(orderedby)]

    
    data = db.list_documents('med-cmc','examenes',queries=queries)
    docs = data

    return docs
        