from appwriteClient import db

def agregar_ad(ad):
    try:
        data = db.create_document('med-cmc','ads',ad)
        return {"message":f"El Anuncio con titulo {ad['titulo']} fue agregado exitosamente","id":data["$id"]}
    except Exception as e:
        return str(e)