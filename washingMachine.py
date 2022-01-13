class WashingMachine ():
    def __init__ (self):
        pass

    def washClothes (self, temperatureWater="cold"):
        self.__fill_water_tank(temperatureWater)
        self.__add_soap()
        self.__wash()
        self.__centrifuge()
    
    def __fill_water_tank (self, temperatureWater):
        print(f"Filling the water tank with {temperatureWater} water")

    def __add_soap (self):
        print(f"Adding Soap to the mix")

    def __wash (self):
        print("Washing the Clothes")

    def __centrifuge (self):
        print("Centrifuging the Clothes")

if __name__ == "__main__":
    machine = WashingMachine()
    machine.washClothes()