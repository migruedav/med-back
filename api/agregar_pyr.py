from appwriteClient import db
import json

def agregar_pyr(id,pyr):
    try:
        data = db.update_document('med-cmc',"examenes",id,json.dumps(pyr))
        return {"message":f"El Post con titulo {pyr['titulo']} fue editado exitosamente","id":data["$id"]}
    except Exception as e:
        return str(e)