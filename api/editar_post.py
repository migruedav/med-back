import json
from appwriteClient import db

def editar_post(post):
    print(post)
    try:
        post_data = json.loads(post['post']['post'])
        db.update_document('med-cmc','posts',post['post']['id'],post_data)
        return "Post editado correctamente"
    except Exception as e:
        return str(e)