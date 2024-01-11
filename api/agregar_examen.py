from appwriteClient import db
import uuid

def agregar_examen(examen):
    id=str(uuid.uuid4())
    try:
        data = db.create_document('med-cmc','examenes',id,examen)
        return {"message":f"El Examen con titulo {examen['titulo']} fue agregado exitosamente","id":data["$id"]}
    except Exception as e:
        return str(e)