from appwriteClient import db
import uuid

def agregar_examen(examen):
    id=str(uuid.uuid4())
    try:
        data = db.create_document('med-cmc','examenes',id,examen)
        return {"id":id}
    except Exception as e:
        return str(e)