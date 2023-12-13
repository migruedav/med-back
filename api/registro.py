from supabaseCl import supabaseClient

def registro(registro):
    try:
        data = supabaseClient.table('web_medicos').insert(registro).execute()
        return data.data
    except Exception as e:
        return e.message
