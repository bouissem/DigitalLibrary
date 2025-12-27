class Book:
    def __init__(self, book_id, title, author):
        self.__id = book_id
        self.__title = title
        self.__author = author
        self.__available = True  # True = disponible, False = emprunté

    # Properties (getters)
    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def available(self):
        return self.__available

    # Setter pour la disponibilité
    @available.setter
    def available(self, status):
        if isinstance(status, bool):
            self.__available = status
        else:
            raise ValueError("Status must be a boolean value")

    # Méthode pour afficher les informations du livre
    def __str__(self):
        status = "Disponible" if self.__available else "Emprunté"
        return f"Book(ID: {self.__id}, Title: '{self.__title}', Author: {self.__author}, Status: {status})"

