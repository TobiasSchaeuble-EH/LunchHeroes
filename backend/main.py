from fastapi import FastAPI
from supabase_client import supabase_client

app = FastAPI()


@app.get("/")
def read_root():
    data = supabase_client.table("category").select("*").execute()
    return {"Hello": "World", "data" : data}
