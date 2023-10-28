from fastapi import FastAPI, HTTPException
from supabase import create_client, Client


# Fetch data from the `users` table that correspond to a specific time range
async def fetch_users_by_time_range(start_time, end_time):

  app = FastAPI()

  # Replace these values with your Supabase project credentials
  SUPABASE_URL = "https://your-supabase-url.supabase.co"
  SUPABASE_ANON_KEY = "your-supabase-anon-key"

  supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

  @app.get("/items/{item_id}")
  async def read_item(item_id: int):
      response = await supabase.table("items").select().eq("id", item_id).execute()
      item = response.get("data")
      if item:
          return item
      raise HTTPException(status_code=404, detail="Item not found")
  
  
