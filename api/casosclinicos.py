from supabaseCl import supabaseClient

def casosclinicos():
    data = supabaseClient.table('posts').select("*").filter("categoria", "eq", "Casos Clínicos").order("id", desc=True).execute()
    return data.data
