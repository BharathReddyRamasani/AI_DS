# delete_book.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def can_delete_book(book_id):
    resp = sb.table("borrow_records").select("*").eq("book_id", book_id).execute()
    borrowed = resp.data
    return not borrowed 

def delete_book(book_id):
    if can_delete_book(book_id):
        resp = sb.table("books").delete().eq("book_id", book_id).execute()
        return resp.data
    else:
        return None

if __name__ == "__main__":
    book_id = input("Enter Book ID to delete: ").strip()

    deleted = delete_book(book_id)
    if deleted:
        print(" Deleted book:", deleted)
    else:
        print(" Cannot delete book — it is currently borrowed or invalid ID.")
