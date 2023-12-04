from supabaseCl import supabaseClient

def borrarvideocurso(id):
    data = supabaseClient.table('video_cursos').delete().eq('id',id).execute()
    data = data.data
    return data