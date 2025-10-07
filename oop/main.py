# main.py
from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)  # Create a book

    print(my_book)        # Uses __str__
    print(repr(my_book))  # Uses __repr__

    del my_book           # Deletes the book and triggers __del__

if __name__ == "__main__":
    main()
