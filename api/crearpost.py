from appwriteClient import db
import uuid

def crearpost(post):
    id = str(uuid.uuid4())
    try:
        data = db.create_document('med-cmc','posts',id,post)
        return id
    except Exception as e:
        return e.message