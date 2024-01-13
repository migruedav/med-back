from supabaseCl import supabaseClient

def registro(registro):
    supabaseClient.table("web_medicos").insert(registro).execute()
    return {"status": "ok"}
