from supabaseCl import supabaseClient

def medicosexamenes():
    data = supabaseClient.table('web_medicosexamenes').select("*").order("fecha_presentacion", desc=True).execute()
    data = data.data
    return data
