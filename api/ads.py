from supabaseCl import supabaseClient

def ads(position):
    data = supabaseClient.table('ads').select("*").filter("visible", "eq", True).order("id", desc=True).execute()
    data = data.data
    data = [x for x in data if position in x['visible_en']]
    return data
