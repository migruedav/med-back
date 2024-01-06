from appwriteClient import db
from appwrite import query
q = query.Query()

def examenes():
    data = db.list_documents('med-cmc','examenes')
    docs = data['documents']
    return docs
