from supabaseCl import supabaseClient

def biblioteca():
    data = supabaseClient.table('posts').select("*").filter("categoria", "eq", "Biblioteca Clínica").order("id", desc=True).execute()
    return data.data
