from supabaseCl import supabaseClient

def destacados():
    data = supabaseClient.table('posts').select("*").filter("es_destacado", "eq", True).order("id", desc=True).execute()
    return data.data