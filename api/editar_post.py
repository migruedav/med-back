from appwriteClient import db

def editar_post(post):
    try:
        data = db.update_document('med-cmc','posts',post['id'],post['post'])
        return "Post editado correctamente"
    except Exception as e:
        return str(e)