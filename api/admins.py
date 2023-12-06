from supabaseCl import supabaseClient

def admins():
    data = supabaseClient.table('admins').select("*").execute()
    data = data.data
    admins =[x['email'] for x in data]
    return admins
