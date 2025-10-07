# book_class.py

class Book:
    # Constructor: runs when we create a book
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor: runs when we delete a book
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation: what we see when we print the book
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation: shows code to recreate the book
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
