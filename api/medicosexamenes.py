from supabaseCl import supabaseClient

def medicosexamenes():
    data = supabaseClient.table('web_medicosexamenes').select("fecha_presentacion,email, examen_id(nombre),puntuacion_obtenida").order("fecha_presentacion", desc=True).execute()
    data = data.data
    return data
