from supabaseCl import supabaseClient

def categoria(cat):
    try:
        data = supabaseClient.table('posts').select("*").eq("categoria",cat).order("id", desc=True).limit(163).execute()
        data = data.data
        return data
    except:
        return {'message':'error'}
