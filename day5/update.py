# import os
# from supabase import create_client, Client  # pip install supabase
# from dotenv import load_dotenv  # pip install python-dotenv

# # Load environment variables from .env
# load_dotenv()

# url = os.getenv("SUPABASE_URL")
# key = os.getenv("SUPABASE_KEY")
# sb: Client = create_client(url, key)

# def up_product(id,stock):
#     resp = sb.table("products").update({"stock": stock}).eq("id",id).execute()
#     return resp.data


# if __name__=="__main__":
#     id=int(input("product id"))
#     stock = int(input("Enter stock: ").strip())
#     updated = up_product(id, stock)
#     print(" Stock Updated:", updated)


# update_stock.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def update_stock(product_id, new_stock):
    resp = sb.table("products").update({"stock": new_stock}).eq("product_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(pid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 
 