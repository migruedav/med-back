from supabaseCl import supabaseClient

def videocursosslider():
    data = supabaseClient.table('video_cursos').select("*").filter("slider", "eq", True).order("id", desc=True).execute()
    data = data.data
    return data
