# list_products.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def list_books():
    resp = sb.table("books").select("*").order("book_id", desc=False).execute()
    return resp.data

def search_book(title):
    resp = sb.table("books").select("*").ilike("title", f"%{title}%").execute()
    return resp.data

def show_member_borrowed_books():
    resp = sb.table("borrow_records")\
        .select("member_id, members(name), books(title, author)")\
        .execute()
    return resp.data


if __name__ == "__main__":
    print("Choose an option:")
    print("1. List all books")
    print("2. Search books by title")
    print("3. Show members and their borrowed books")
    choice = input("Enter choice [1/2/3]: ").strip()

    if choice == "1":
        books = list_books()
        if books:
            print(" All Books:")
            for b in books:
                print(f"{b['book_id']}: {b['title']} (author: {b['author']}) — {b['category']} — stock: {b['stock']}")
        else:
            print("📌 No books found.")

    elif choice == "2":
        title_search = input("Enter title to search: ").strip()
        results = search_book(title_search)
        if results:
            print(f" Search results for '{title_search}':")
            for b in results:
                print(f"{b['book_id']}: {b['title']} (author: {b['author']}) — {b['category']} — stock: {b['stock']}")
        else:
            print(f" No books found with title containing '{title_search}'.")

    elif choice == "3":
        borrowed = show_member_borrowed_books()
        if borrowed:
            print(" Members and their borrowed books:")
            for entry in borrowed:
                member_name = entry['members']['name']
                book_title = entry['books']['title']
                book_author = entry['books']['author']
                print(f"{member_name} borrowed '{book_title}' by {book_author}")
        else:
            print(" No borrow records found.")

    else:
        print(" Invalid choice. Please enter 1, 2, or 3.")
