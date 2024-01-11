from appwriteClient import db
import json

def agregar_pyr(post):
    try:
        data = db.update_document('med-cmc', "examenes", post['id'], post['pyr'])
        return "Preguntas y respuestas agregadas exitosamente"
    except Exception as e:
        return str(e)