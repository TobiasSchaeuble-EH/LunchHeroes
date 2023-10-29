

from fastapi.encoders import jsonable_encoder
from src.lunchheros.db.dbFetcher import get_encoded_data
from src.routes.users.userFunctions import getAllUsers, getUserWithId
from fastapi import FastAPI
from supabase_client import supabase_client

app = FastAPI()


@app.get("/")
def read_root():
    data = supabase_client.table("category").select("*").execute()
    return {"Hello": "World", "data" : data}

@app.get("/users")
def load_all_users():
    allUsers = getAllUsers()
    return { "allUsers" : allUsers}

@app.get("/users/{userId}")
def load_current_user(userId):
    currentUser = getUserWithId(userId)
    return { "currentUser" : currentUser}

@app.get("/button_trigger/{userId}")
def load_current_user(userId: str):
    userData = getUserWithId(userId)
    print("asdas")
    #test =  get_encoded_data(1,1,userData)

    return { "currentUser" : userData}