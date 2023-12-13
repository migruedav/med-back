from supabaseCl import supabaseClient


def registro(registro):
    try:
        data = supabaseClient.table('web_medicos').insert({
            'nombre': registro['nombre'],
            'apellido': registro['apellido'],
            'email': registro['email'],
            'cedula': registro['cedula'],
            'especialidad': registro['especialidad'],
            'pais': registro['pais'],
            'estado': registro['estado']
        }).execute()
        if data['status'] == 201:
            supabaseClient.auth.sign_up(
                registro['email'], registro['password'])
            return data
        else:
            return data
    except Exception as e:
        return e.message
