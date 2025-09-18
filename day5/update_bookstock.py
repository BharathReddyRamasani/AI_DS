# update_stock.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def update_stock(product_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("title", title).execute()
    return resp.data
 
if __name__ == "__main__":
    title=input("enter title").strip()
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(title, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 
 