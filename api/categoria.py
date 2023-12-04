from supabaseCl import supabaseClient

def categoria(cat):
    try:
        data = supabaseClient.table('posts').select("*").eq("categoria",cat).eq("visible",True).order("fecha", desc=True).limit(160).execute()
        data = data.data
        return data
    except:
        return {'message':'error'}
