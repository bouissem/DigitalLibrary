class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name

    # Properties
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    # Optional: afficher info utilisateur
    def __str__(self):
        return f"User(ID: {self.__id}, Name: {self.__name})"
