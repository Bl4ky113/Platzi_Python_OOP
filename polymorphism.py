class Person:
    def __init__ (self, name):
        self.name = name

    def move_to (self, place):
        print(f"walking to {place}")

class Ciclyst (Person):
    def __init__ (self, name):
        super().__init__(name)

    def move_to (self, place):
        print(f"Biking to {place}")

class Driver (Person):
    def __init__ (self, name):
        super().__init__(name)

    def move_to (self, place):
        print(f"Driving to {place}")

if __name__ == "__main__":
    p1 = Person("1")
    p2 = Ciclyst("2")
    p3 = Driver("3")

    p1.move_to("grocery Store")
    p2.move_to("grocery Store")
    p3.move_to("grocery Store")