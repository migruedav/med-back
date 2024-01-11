from appwriteClient import db
import uuid

def subir_imagen(imagen,bucket):
    id = str(uuid.uuid4())
    try:
        data = db.create_file('med-cmc', bucket,id, imagen)
        return data['$id']
    except Exception as e:
        return e.message