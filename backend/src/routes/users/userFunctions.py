from supabase_client import supabase_client


users_select = "*, company:companies(*), users_interests(*, interest(*, category(*))), age_range(*)"

def getUserWithId(userId):
    return supabase_client.table("users").select(users_select).eq("id", userId).single().execute()


def getAllUsers():
    return  supabase_client.table("users").select(users_select).execute()
    
