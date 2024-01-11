from appwriteClient import db

def borrar_ad(id):
    try:
        data = db.delete_document('med-cmc','ads',id)
        return {"message":f"El Anuncio con id {id} fue borrado exitosamente"}
    except Exception as e:
        return e.message