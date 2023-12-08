from supabase import create_client
surl = "https://oogloklbnjeivsuibzgv.supabase.co"
sanon = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9vZ2xva2xibmplaXZzdWliemd2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDE5OTU5ODcsImV4cCI6MjAxNzU3MTk4N30.74XP_KGp9HRNpKTi3TKpR9htKOqHFnpFTas7uTthvFM"

supabaseClient = create_client(surl, sanon)

def all_posts(limit=100):

    data = supabaseClient.table('posts').select("*").limit(limit).execute()
    data = data.data
        
    return data
    