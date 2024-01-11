from appwriteClient import db
from appwrite import query
q = query.Query()

def all_ads():
    data = db.list_documents('med-cmc','ads')
    docs = data['documents']
    return docs

