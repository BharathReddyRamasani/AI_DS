import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def add_member(name, email):
    payload = {"name": name, "email":email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data


if __name__ == "__main__":
    n = int(input("How many members do you want to add? ").strip())

    for i in range(n):
        print(f"\n--- members {i+1} ---")
        name = input("Enter  name: ").strip()
        email=input("enter email").strip()

        created = add_member(name, email)
        print("🚀 Inserted:", created)
