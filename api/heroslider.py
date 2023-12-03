from supabaseCl import supabaseClient

def heroslider():
    return supabaseClient.table('posts').select("titulo,autor,imagen, slug").filter("hero_slider", "eq", True).order("id", desc=True).execute()
