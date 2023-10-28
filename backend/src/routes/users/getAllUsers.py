from supabase_client import supabase_client

def getAllUsers():
    data = supabase_client.table("users").select("*, company:companies(*)").execute()
    return data;