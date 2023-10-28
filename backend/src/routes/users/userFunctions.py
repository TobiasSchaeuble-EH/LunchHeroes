from supabase_client import supabase_client


users_select = "*, company:companies(*)"

def getUserWithId(userId):
    return supabase_client.table("users").select(users_select).eq("id", userId).single().execute()

from supabase_client import supabase_client

def getAllUsers():
    return  supabase_client.table("users").select(users_select).execute()
    