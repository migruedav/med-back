from appwriteClient import db

def agregar_pyr(id,pyr):
    try:
        data = db.update_document()('med-cmc',"examenes",id,pyr)
        return {"message":f"El Post con titulo {pyr['titulo']} fue editado exitosamente","id":data["$id"]}
    except Exception as e:
        return str(e)