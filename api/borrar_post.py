from appwriteClient import db

def borrar_post(id):
    try:
        data = db.delete_document('med-cmc','posts',id)
        return {"message":f"El Post con id {id} fue borrado exitosamente"}
    except Exception as e:
        return e.message