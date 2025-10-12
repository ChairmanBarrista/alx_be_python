# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class initializer
        self.file_size = file_size       # Unique attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class initializer
        self.page_count = page_count     # Unique attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition — manages a collection of books."""

    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook objects

    def add_book(self, book):
        """Add a book instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Display all books currently in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
