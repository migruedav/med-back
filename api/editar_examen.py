from appwriteClient import db

def editar_examen(examen):
    try:
        data = db.update_document('med-cmc','examenes',examen['id'],examen['examen'])
        return {"message":f"El examen con titulo {examen['titulo']} fue editado exitosamente","id":id}
    except Exception as e:
        return e.message