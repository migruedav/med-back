from appwriteClient import db
import json

def agregar_pyr(post):
    try:
        pyr = json.dumps(post['pyr'])
        data = db.update_document('med-cmc', "examenes", post['id'], {"preguntas_y_respuestas": pyr})
        return "Preguntas y respuestas agregadas exitosamente"
    except Exception as e:
        return str(e)