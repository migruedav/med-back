from supabaseCl import supabaseClient

def heroslider():
    return supabaseClient.table('posts').select('*').limit(1).execute()