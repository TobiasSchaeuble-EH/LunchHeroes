import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
print(url, key)
supabase_client: Client = create_client(url, key)
