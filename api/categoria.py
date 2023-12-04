from supabaseCl import supabaseClient

def categoria(cat):
    data = supabaseClient.table('posts').select("*").eq("categoria",cat).order("id", desc=True).execute()
    data = data.data
    return data
