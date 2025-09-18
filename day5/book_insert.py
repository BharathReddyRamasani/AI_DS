import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def add_book(title,author,categeory,stock):
    payload = {"title":title, "author":author,"category":categeory,"stock":stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data


if __name__ == "__main__":
    n = int(input("How many books do you want to add? ").strip())

    for i in range(n):
        print(f"\n--- books {i+1} ---")
        title = input("Enter  title: ").strip()
        author=input("enter author").strip()
        categeory=input("enter categeory").strip()
        stock=int(input("enter stock").strip())
        created = add_book(title,author,categeory,stock)
        print("Inserted:", created)
