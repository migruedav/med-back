from supabaseCl import supabaseClient

def crearpost(post):
    data = supabaseClient.table('posts').insert(post)
    return data.data