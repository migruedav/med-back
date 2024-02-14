from supabaseCl import supabaseClient


def crearusuario(usuario):
    supabaseClient.auth.sign_up(
        {
            "email": usuario["email"],
            "password": usuario["password"],
            "options": {
                "data": {
                    "nombre": usuario["nombre"],
                    "apellido": usuario["apellido"],
                    "cedula": usuario["cedula"],
                    "especialidad": usuario["especialidad"],
                    "pais": usuario["pais"],
                    "estado": usuario["estado"],
                }
            },
        }
    )
    return {"status": "ok"}
