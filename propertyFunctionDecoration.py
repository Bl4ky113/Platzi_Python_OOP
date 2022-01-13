from types import new_class


class function_decoration_test ():
    def __init__ (self):
        self.__private_1 = "perro"
        self.__private_2 = "hello"
        self.__private_3 = "gato"

    @property
    def private_1 (self):
        """ 1st Example of the property function decoration method """
        return self.__private_1

    @private_1.setter
    def private_1 (self, new_value=""):
        self.__private_1 = new_value.upper()

    @private_1.deleter
    def private_1 (self):
        del self.__private_1

    @property
    def private_2 (self):
        """ 2nd Example of the property function decoration method """
        return self.__private_2

    @private_2.setter
    def private_2 (self, new_value=""):
        self.__private_2 = new_value.lower()

    @private_2.deleter
    def private_2 (self):
        del self.__private_2

    @property
    def private_3 (self):
        """ 3rd Example of the property function decoration method """
        return self.__private_3

    @private_3.setter
    def private_3 (self, new_value=""):
        self.__private_3 = new_value.capitalize()

    @private_3.deleter
    def private_3 (self):
        del self.__private_3

if __name__ == "__main__":
    new_obj = function_decoration_test()

    print(new_obj.private_1)
    new_obj.private_1 = "bonito"
    print(new_obj.private_1)
    print(new_obj.private_2)
    new_obj.private_2 = "BONITO"
    print(new_obj.private_2)
    print(new_obj.private_3)
    new_obj.private_3 = "BONITO"
    print(new_obj.private_3)

    del new_obj.private_1
    del new_obj.private_2
    del new_obj.private_3
    print(new_obj.private_1)
    print(new_obj.private_2)
    print(new_obj.private_3)