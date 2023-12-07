from supabaseCl import supabaseClient

def especialidad(esp):

    try:
        data = supabaseClient.table('posts').select("*").filter("visible","eq",True).order("fecha", desc=True).limit(100).execute()
        data = data.data
        data = [x for x in data if esp==x['especialidad_principal'] or esp in x['otras_especialidades']]
        return data
    except:
        return {'message':'error'}
