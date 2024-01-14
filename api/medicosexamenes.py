from appwriteClient import db,q

def medicosexamenes():
    data = db.list_documents('med-cmc','examenes_aprobados',[q.order_desc('fecha'),q.limit(10000)])
    data = data['documents']
    return data
