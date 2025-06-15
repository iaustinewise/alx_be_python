class Book:
    """A class representing a book with title, author, and checkout status."""

    def __init__(self, title, author):
        """Initialize a Book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return the availability status of the book."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        """Initialize an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
