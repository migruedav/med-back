from supabaseCl import supabaseClient

def crearusuario(usuario):
    supabaseClient.auth.sign_up({
        "email": usuario['email'],
        "password": usuario['password'],
    })
    return {"status": "ok"}
