from books import show_books, load_books, save_books
from dotenv import load_dotenv
import os

load_dotenv()

admin_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    password = input("enter the admin password: ")
    if password == admin_password:
        print("entered admin mode")
    else:
        print("wrong password")

name = input("what is your name? ")
print("welcome", name)

count = int(input("how many books do you want to enter? "))
books = load_books()

for i in range(count):
    book = input("enter the name of book: ") 
    books.append(book)

show_books(books)
save_books(books)