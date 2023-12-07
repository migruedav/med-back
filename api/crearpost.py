from supabaseCl import supabaseClient

def crearpost(post):
    try:
        data = supabaseClient.table('posts').insert(post).execute()
        return data.data
    except Exception as e:
        return e.message
    
