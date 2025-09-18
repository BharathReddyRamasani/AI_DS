
# update_stock.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def update_stock(name, email):
    resp = sb.table("members").update({"email": new_email}).eq("name", name).execute()
    return resp.data
 
if __name__ == "__main__":
    name = (input("Enter product_id to update: ").strip())
    new_email = (input("Enter new stock value: ").strip())
 
    updated = update_stock(name, new_email)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 
 