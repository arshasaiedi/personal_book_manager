from books import show_books

name = input("what is your name? ")
print("welcome", name)

count = int(input("how many books do you want to enter? "))
books = []

for i in range(count):
    book = input("enter the name of book: ") 
    books.append(book)

show_books(books)