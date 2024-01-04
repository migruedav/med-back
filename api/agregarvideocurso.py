from supabaseCl import supabaseClient

def agregarvideocurso(titulo, video, imagen, slider):
    data = supabaseClient.table('video_cursos').insert({"titulo":titulo,"video":video,"imagen":imagen,"slider":slider}).execute()
    data = data.data
    return data 