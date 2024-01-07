from supabaseCl import supabaseClient
from appwriteClient import db
from appwrite import query
from api.examenes import examenes
q = query.Query()


def examenes_aprovados(email,all_exams):
    data = supabaseClient.table("web_medicosexamenes").select("examen_id,fecha_presentacion,puntuacion_obtenida").eq("email", email).execute()
    data = data.data
    for i in data:
        for j in all_exams:
            if i['examen_id'] == j['prev_id']:
                i['slug'] = j['slug']
                i['nombre'] = j['nombre']
                i['imagen'] = j['imagen']
    
    
    return data

