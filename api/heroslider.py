from supabaseCl import supabaseClient

def heroslider():
    data = supabaseClient.table('posts').select("titulo,autor,imagen, slug").filter("visible","eq",True).filter("hero_slider", "eq", True).order("id", desc=True).execute()
    return data.data