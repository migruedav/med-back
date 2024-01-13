from appwriteClient import db,q
import uuid

def agregar_examen_aprobado(examen):
    id=str(uuid.uuid4())
    id_medico = db.list_documents('med-cmc','medicos',[q.equal('email',examen['email'])])
    id_medico = id_medico['documents'][0]['$id']
    examen['medicos'] = id_medico
    try:
        data = db.create_document('med-cmc','examenes_aprobados',id,examen)
        return {"id":id}
    except Exception as e:
        return str(e)