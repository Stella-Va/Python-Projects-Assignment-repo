class LibraryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Book class (Base Class)
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # Initially, the book is not borrowed

    def borrow(self):
        if self.is_borrowed:
            raise LibraryException(f"The book '{self.title}' is already borrowed!")
        self.is_borrowed = True
        print(f"Book '{self.title}' has been borrowed!")

    def return_book(self):
        if not self.is_borrowed:
            raise LibraryException(f"The book '{self.title}' was not borrowed!")
        self.is_borrowed = False
        print(f"Book '{self.title}' has been returned!")

# RegularUser Class (Subclass of User)
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # A list to keep track of borrowed books

    def borrow_book(self, book):
        try:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        except LibraryException as e:
            print(f"Error: {e}")

    def return_book(self, book):
        try:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        except LibraryException as e:
            print(f"Error: {e}")

# AdminUser Class 
class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    # Admin can add books to the library
    def add_book_to_library(self, library, book):
        library.add_book(book)
        print(f"Admin {self.name} added '{book.title}' to the library.")

# Library class
class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"'{book.title}' by {book.author} ({status})")

# Main Program
if __name__ == "__main__":
    # Creating some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book4 = Book("Think Big", "Ben Carson", "9780061420084")

    # library to add books to it
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)


    # Creating a regular user
    user = User("Alice")

    # Creating an admin user
    admin = AdminUser("Bob")

    # Admin adds a new book to the library
    print("\nAdmin adds a book:")
    admin.add_book_to_library(library, Book("Moby Dick", "Herman Melville", "9780142437247"))

    # List books in the library
    print("\nListing books in the library:")
    library.list_books()

    # User borrows a book
    print("\nAlice borrows '1984':")
    user.borrow_book(book2)

    # List books again to see the status change
    print("\nListing books in the library after borrowing:")
    library.list_books()

    # User returns the book
    print("\nAlice returns '1984':")
    user.return_book(book2)

    # List books again to see the status change
    print("\nListing books in the library after returning:")
    library.list_books()
