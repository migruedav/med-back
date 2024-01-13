from appwriteClient import db
import uuid

def agregar_medico(medico):
    id = str(uuid.uuid4())
    try:
        new_medico = db.create_document('med-cmc','medicos',id,medico)
        return new_medico
    except Exception as e:
        return e
