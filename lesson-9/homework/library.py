# Custom Exceptions
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"{self.title} by {self.author} is already borrowed."
            )
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


# Member class
class Member:
    MAX_BOOKS_ALLOWED = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BOOKS_ALLOWED:
            raise MemberLimitExceededException(
                f"{self.name} has reached the maximum limit of borrowed books."
            )
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(
                f"{self.name} did not borrow {book.title} by {book.author}."
            )


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if member is None:
            raise ValueError(f"Member '{member_name}' not found in the library.")

        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            raise BookNotFoundException(
                f"Book '{book_title}' not found in the library."
            )

        try:
            book.borrow()
            member.borrow_book(book)
            print(f"{member_name} borrowed '{book_title}' successfully.")
        except BookAlreadyBorrowedException as e:
            print(e)
        except MemberLimitExceededException as e:
            print(e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if member is None:
            raise ValueError(f"Member '{member_name}' not found in the library.")

        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            raise BookNotFoundException(
                f"Book '{book_title}' not found in the library."
            )

        try:
            member.return_book(book)
            book.return_book()
            print(f"{member_name} returned '{book_title}' successfully.")
        except BookNotFoundException as e:
            print(e)


# Testing the library system
if __name__ == "__main__":
    # Create books
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Create members
    member1 = Member("Alice")
    member2 = Member("Bob")

    # Create library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add members to the library
    library.add_member(member1)
    library.add_member(member2)

    # Test borrowing and returning books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "1984")  # Testing BookAlreadyBorrowedException
    except BookAlreadyBorrowedException as e:
        print(e)

    library.borrow_book("Bob", "To Kill a Mockingbird")
    library.borrow_book(
        "Alice", "To Kill a Mockingbird"
    )  # Testing MemberLimitExceededException

    library.return_book("Alice", "1984")
    library.return_book("Bob", "To Kill a Mockingbird")
    library.return_book("Bob", "To Kill a Mockingbird")  # Testing BookNotFoundException
