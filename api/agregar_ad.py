from appwriteClient import db
import uuid

def agregar_ad(ad):
    id=str(uuid.uuid4())
    try:
        data = db.create_document('med-cmc','ads',id,ad)
        return {"message":f"El Anuncio con titulo {ad['titulo']} fue agregado exitosamente","id":data["$id"]}
    except Exception as e:
        return str(e)