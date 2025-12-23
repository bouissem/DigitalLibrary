class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
