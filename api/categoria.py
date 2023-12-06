from supabaseCl import supabaseClient

def categoria(cat):
    try:
        data = supabaseClient.table('posts').select("*").filter("visible","eq",True).eq("categoria",cat).order("fecha", desc=True).limit(100).execute()
        data = data.data
        return data
    except:
        return {'message':'error'}
