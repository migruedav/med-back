from appwriteClient import db
import json

def agregar_pyr(id, pyr):
    try:
        pyr = json.loads(pyr)
        doc = {"preguntas_y_respuestas": pyr}
        data = db.update_document('med-cmc', "examenes", id, doc)
        return "Preguntas y respuestas agregadas exitosamente"
    except Exception as e:
        return str(e)