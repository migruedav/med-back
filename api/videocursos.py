from supabaseCl import supabaseClient

def videocursos(slider: bool = False):
    data = supabaseClient.table('video_cursos').select("*").order("id", desc=True).execute()
    data = data.data
    return data
