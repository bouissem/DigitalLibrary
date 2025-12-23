from book import Book
from user import User
from loan import Loan


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__loans = []

    # -------- Books --------
    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book_id):
        self.__books = [b for b in self.__books if b.get_id() != book_id]

    # -------- Users --------
    def register_user(self, user):
        self.__users.append(user)

    # -------- Loans --------
    def borrow_book(self, book_id, user_id):
        book = None
        user = None

        for b in self.__books:
            if b.get_id() == book_id and b.is_available():
                book = b
                break

        for u in self.__users:
            if u.get_id() == user_id:
                user = u
                break

        if book and user:
            book.set_available(False)
            loan = Loan(book, user)
            self.__loans.append(loan)
            print("Book borrowed successfully.")
        else:
            print("Borrowing failed.")

    def return_book(self, book_id):
        for loan in self.__loans:
            if loan.get_book().get_id() == book_id and not loan.is_returned():
                loan.return_book()
                loan.get_book().set_available(True)
                print("Book returned successfully.")
                return

        print("No active loan found for this book.")

    # -------- Display --------
    def display_status(self):
        print("\nBooks:")
        for b in self.__books:
            status = "Available" if b.is_available() else "Borrowed"
            print(f"{b.get_id()} - {b.get_title()} ({status})")

        print("\nActive Loans:")
        for l in self.__loans:
            if not l.is_returned():
                print(f"{l.get_book().get_title()} borrowed by {l.get_user().get_name()}")
