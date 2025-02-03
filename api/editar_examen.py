from appwriteClient import db


def editar_examen(examen):
    print(examen)
    try:
        data = db.update_document("med-cmc", "examenes", examen["id"], examen["examen"])
        return examen["id"]
    except Exception as e:
        return str(e)
