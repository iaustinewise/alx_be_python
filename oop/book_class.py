class Book:
    """A class representing a book with title, author, and publication year using magic methods."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string representation that could recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
