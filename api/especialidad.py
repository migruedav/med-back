from appwriteClient import db
from appwrite import query
q = query.Query()

def especialidad(esp):
    queries = [q.equal('especialidad_principal',esp),q.equal("visible",True),q.order_desc('$createdAt')]
    data = db.list_documents('med-cmc','posts',queries=queries)
    docs = data['documents']
    docs = [x for x in docs if esp==x['especialidad_principal'] or esp in x['otras_especialidades']]
    return docs
