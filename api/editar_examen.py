from appwriteClient import db


def editar_examen(examen):
    print(examen["id"])
    print(examen["examen"])

    try:
        data = db.update_document("med-cmc", "examenes", examen["id"], examen["examen"])
        print(data)
        return examen["id"]
    except Exception as e:
        return str(e)
