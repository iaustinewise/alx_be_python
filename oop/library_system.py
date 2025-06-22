class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """Class to manage a collection of books using composition."""

    def __init__(self):
        """Initialize an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book instance to the library."""
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
            return True
        return False

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
