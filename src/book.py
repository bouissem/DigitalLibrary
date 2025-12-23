class Book:
    def __init__(self, book_id, title, author):
        self.__id = book_id
        self.__title = title
        self.__author = author
        self.__available = True

    # Getters
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    # Setters
    def set_available(self, status):
        self.__available = status
