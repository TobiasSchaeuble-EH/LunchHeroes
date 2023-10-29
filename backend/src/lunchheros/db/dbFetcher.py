from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv   
import numpy as np
import pandas as pd
import json
import os 

# Load environment variables from .env file
load_dotenv()                    

# Get the credentials from the environment variables
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY')

# Create a Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Create a FastAPI app
app = FastAPI()

@app.get("/encoded_data/{time_slot}/{location}")
async def get_encoded_data(time_slot: int, location: str):
    # Fetch data
    response = await supabase.table("items").select().eq("time_slot", time_slot).eq("location", location).execute()
    data = response.get("data")
    
    if not data:
        raise HTTPException(status_code=404, detail="Data not there")
    
    # Transform data
    df = pd.DataFrame(data)
    
    # One-hot encode data
    one_hot_encoded_df = pd.get_dummies(df, columns=['WIP'])  # wip - replace with actual column names
    #one_hot_encoded_df.to_dict(orient='records') 

    return one_hot_encoded_df
