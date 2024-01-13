from appwriteClient import db,q

def examenes_aprobados(mail):

    queries =[q.equal('email',mail)]
    id = db.list_documents('med-cmc','medicos',queries)
    id = id['documents'][0]['$id']
    queries =[q.equal('medicos',id)]
    examenes = db.list_documents('med-cmc','examenes_aprobados',queries)
    examenes = examenes['documents']

    return examenes
