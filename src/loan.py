class Loan:
    def __init__(self, book, user):
        self.__book = book
        self.__user = user
        self.__returned = False

    # Getters
    def get_book(self):
        return self.__book

    def get_user(self):
        return self.__user

    def is_returned(self):
        return self.__returned

    # Mark loan as returned
    def return_book(self):
        self.__returned = True
