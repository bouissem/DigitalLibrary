class Loan:
    def __init__(self, book, user):
        self.__book = book
        self.__user = user
        self.__returned = False

    # Properties
    @property
    def book(self):
        return self.__book

    @property
    def user(self):
        return self.__user

    @property
    def returned(self):
        return self.__returned

    # Mark loan as returned
    def return_book(self):
        self.__returned = True

    # Optional: afficher info du prêt
    def __str__(self):
        status = "Returned" if self.__returned else "Active"
        return f"Loan(Book: {self.__book.title}, User: {self.__user.name}, Status: {status})"
