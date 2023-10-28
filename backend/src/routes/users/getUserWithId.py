from supabase_client import supabase_client

def getUserWithId(userId):
    return supabase_client.table("users").select("*").eq("id", userId).execute()