from appwriteClient import db
import uuid

def crearpost(post):
    id = str(uuid.uuid4())
    try:
        data = db.create_document('med-cmc','posts',id,post)
        return f"El Post con titulo {post['titulo']} fue creado exitosamente"
    except Exception as e:
        return e.message