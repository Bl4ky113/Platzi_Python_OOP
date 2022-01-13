class Coordinates:
    def __init__ (self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def calcDistance (self, otherCoords):
        if isinstance(otherCoords, Coordinates):
            x_distance = (self.x - otherCoords.x) ** 2
            y_distance = (self.y - otherCoords.y) ** 2

            return (x_distance + y_distance) ** 0.5

        else:
            print("Extra Coodinates must be a Coordinates() Instance")
            return None

if __name__ == "__main__":
    coords_1 = Coordinates(0, 0)
    coords_2 = Coordinates(3, 3)

    print(coords_1.calcDistance(coords_2))

