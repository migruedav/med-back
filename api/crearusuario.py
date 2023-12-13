from supabaseCl import supabaseClient

def registro(usuario):
    supabaseClient.auth.sign_up({
        "email": usuario['email'],
        "password": usuario['password'],
    })
    return {"status": "ok"}
