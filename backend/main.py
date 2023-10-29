 


from datetime import datetime
from fastapi.encoders import jsonable_encoder
from src.lunchheros.db.dbFetcher import filter_data
from src.routes.users.userFunctions import get_meeting_data, getAllQueryListData, getAllUsers, getUserWithId
from fastapi import FastAPI
from supabase_client import supabase_client

app = FastAPI()


@app.get("/")
def read_root():
    today = datetime.today().date()
    data = supabase_client.table("category").select("*").execute()
    return {"Hello": "World", "data" : today}

@app.get("/users")
def load_all_users():
    allUsers = getAllUsers()
    return { "allUsers" : allUsers}

@app.get("/users/{userId}")
def load_current_user(userId):
    currentUser = getUserWithId(userId)
    return { "currentUser" : currentUser}

@app.get("/button_trigger/{userId}/{time_slot}")
def load_current_user(userId: str, time_slot: int):
    userData = getUserWithId(userId)
    companyId = userData.data["company"]["id"]
    age_rangeId = userData.data["age_range"]["id"]
    time_rangeId = time_slot
    today = datetime.today().date()

    #python try catch
    data = ""
    try:
        data = supabase_client.table("query_waiting").insert([{"user": userId, "date": today, "company" :companyId , "age_range":age_rangeId, "time_range":time_rangeId, }]).execute()

    except(Exception):
        print("error")
    
     
    queryList = getAllQueryListData()[1]

    test = filter_data(queryList)

    for index, item in enumerate(test):
        print(len(item))
        for indexUsers, user in enumerate(item):
            print(user)
            data = ""
            try:
                data = supabase_client.table("meetings").insert([{ "id":index , "date": today, "time_slot" :time_rangeId, "location" :companyId, "status": 0, "user":user}]).execute()

            except(Exception):
                print("error")

            print(data)

    return { "currentUser" : userData, "query": queryList, "test": test}

@app.get("/get_meeting_data/{userId}")
def get_meeting_data_main(userId: str):
    data, count = get_meeting_data(userId)
    return { "data" : data, "count": count}