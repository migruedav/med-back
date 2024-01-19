from appwriteClient import db

def editar_post(post):
    try:
        data = db.update_document('med-cmc','posts',post['id'],post['post'])
        return {"message":f"El Post con titulo {post['titulo']} fue editado exitosamente","id":id}
    except Exception as e:
        return str(e)