from appwriteClient import db,q

def medicosexamenes():
    data = db.list_documents('med-cmc','examenes_aprobados',[q.order_desc('fecha')])
    data = data['documents']
    return data
