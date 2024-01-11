from appwriteClient import db

def borrar_examen(id):
    try:
        data = db.delete_document('med-cmc','examenes',id)
        return {"message":f"El Examen con id {id} fue borrado exitosamente"}
    except Exception as e:
        return e.message