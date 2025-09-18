# delete_member.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def can_delete_member(member_id):
    resp = sb.table("borrow_records").select("*").eq("member_id", member_id).execute()
    borrowed = resp.data
    return not borrowed 

def delete_member(member_id):
    if can_delete_member(member_id):
        resp = sb.table("members").delete().eq("member_id", member_id).execute()
        return resp.data
    else:
        return None

if __name__ == "__main__":
    member_id = input("Enter member ID to delete: ").strip()

    deleted = delete_member(member_id)
    if deleted:
        print(" Deleted member:", deleted)
    else:
        print(" Cannot delete member — they have borrowed books or invalid ID.")
