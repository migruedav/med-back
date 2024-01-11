from appwriteClient import db
import json

def agregar_pyr(id, pyr):
    try:
        pyr = json.loads(pyr)
        doc = {"preguntas_y_respuestas": pyr}
        data = db.update_document('med-cmc', "examenes", id, doc)
        return {"message": f"El Post con titulo {pyr['titulo']} fue editado exitosamente", "id": data["$id"]}
    except Exception as e:
        return str(e)