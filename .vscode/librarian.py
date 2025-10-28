# Project Overview:
# Create a simple library management system where users can add, view, update, and delete 
# books in a file named `the_librarian.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)
# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.

library = [
    {
        "Title": "To Kill A Mockingbird",
        "Author": "Harper Lee",
        "Year": 1960,
        "ISBN": "978-0-06-112008-4",
        "Available": True
    },
    {
        "Title": "1984",
        "Author": "George Orwell",
        "Year": 1949,
        "ISBN": "978-0-452-28423-4",
        "Available": True
    },
    {
        "Title": "The Great Gatsby",
        "Author": "F. Scott Fitzgerald",
        "Year": 1925,
        "ISBN": "978-0-7432-7356-5",
        "Available": False
    }
]


def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter ISBN: ")
    available = bool(int(input("Is the book available? (1 for Yes, 0 for No): ")))

    new_book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "ISBN": isbn,
        "Available": available
    }
    library.append(new_book)
    print(f'Book "{title}" added successfully.')


def view_books():
    for book in library:
        print(book)

def update_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            book["Title"] = input("Enter new title: ")
            book["Author"] = input("Enter new author: ")
            book["Year"] = int(input("Enter new year of publication: "))
            book["Available"] = bool(int(input("Is the book available? (1 for Yes, 0 for No): ")))
            print(f'Book with ISBN {isbn} updated successfully.')
            break
    else:
         print(f'Book with ISBN {isbn} not found.')

def delete_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print(f'Book with ISBN {isbn} deleted successfully.')
            break
    else:
         print(f'Book with ISBN {isbn} not found.')

def search_book(title):
    for book in library:
        if book["Title"].lower() == title.lower():
            print(book)
            break
    else:
         print(f'Book titled "{title}" not found.')

def borrow_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print(f'You have borrowed "{book["Title"]}".')
            else:
                print(f'Sorry, "{book["Title"]}" is currently not available.')
            break
    else:
         print(f'Book with ISBN {isbn} not found.')

def return_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            book["Available"] = True
            print(f'You have returned "{book["Title"]}".')
            break
    else:
         print(f'Book with ISBN {isbn} not found.')

while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        isbn = input("Enter ISBN of the book to update: ")
        update_book(isbn)
    elif choice == '4':
        isbn = input("Enter ISBN of the book to delete: ")
        delete_book(isbn)
    elif choice == '5':
        title = input("Enter title of the book to search: ")
        search_book(title)
    elif choice == '6':
        isbn = input("Enter ISBN of the book to borrow: ")
        borrow_book(isbn)
    elif choice == '7':
        isbn = input("Enter ISBN of the book to return: ")
        return_book(isbn)
    elif choice == '8':
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")