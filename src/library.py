from book import Book
from user import User
from loan import Loan


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__loans = []

    # -------- Books --------
    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, book_id):
        self.__books = [b for b in self.__books if b.id != book_id]

    # -------- Users --------
    def register_user(self, user: User):
        self.__users.append(user)

    # -------- Loans --------
    def borrow_book(self, book_id, user_id):
        book = next((b for b in self.__books if b.id == book_id and b.available), None)
        user = next((u for u in self.__users if u.id == user_id), None)

        if book and user:
            book.available = False
            loan = Loan(book, user)
            self.__loans.append(loan)
            print("Book borrowed successfully.")
        else:
            print("Borrowing failed.")

    def return_book(self, book_id):
        for loan in self.__loans:
            if loan.book.id == book_id and not loan.returned:
                loan.return_book()
                loan.book.available = True
                print("Book returned successfully.")
                return

        print("No active loan found for this book.")

    # -------- Display --------
    def display_status(self):
        print("\nBooks:")
        for b in self.__books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.id} - {b.title} ({status})")

        print("\nActive Loans:")
        for l in self.__loans:
            if not l.returned:
                print(f"{l.book.title} borrowed by {l.user.name}")
