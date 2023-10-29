from datetime import datetime
from supabase_client import supabase_client


users_select = "*, company:companies(*), users_interests(*, interest(*, category(*))), age_range(*)"

def getUserWithId(userId):
    return supabase_client.table("users").select(users_select).eq("id", userId).single().execute()


def getAllUsers():
    return  supabase_client.table("users").select(users_select).execute()
    

def getAllQueryListData():
    #return  supabase_client.table("waiting_query").select(f"*, user({users_select}), time_range(*), company(*), age_range(*)").execute()
    data, count =  supabase_client.table("query_waiting").select("id:user").execute()
    return data

def get_meeting_data(userId):
    
    #create today date
    #return  supabase_client.table("waiting_query").select(f"*, user({users_select}), time_range(*), company(*), age_range(*)").execute()
    data =  supabase_client.table("meetings").select("*").eq("user", userId).single().execute()
     
    id = data.data["id"]

    data, count = supabase_client.table("meetings").select("*, time_slot(*), location(*)",count='exact').eq("id", id).execute()
 
    return data[1],count
    
