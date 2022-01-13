class Printer ():
    def __init__ (self, ink_storage):
        self.ink_storage = ink_storage
        self.__ink_on_pencil = 20

    def print_file (self, file):
        self.__get_paper()
        self.__fill_ink_in_pencil()
        self.__move_pencil(init=True)
        self.__print(file)
        self.__throw_paper()

    def __get_paper(self):
        paper_available = self.__check_paper()

        if paper_available:
            print("Paper Available for Printing")
        else:
            print("Paper Not Available for Printing")
            raise Exception("Paper Not Available")

    def __check_paper(self):
        paper = " 'Scan of the Printer's Paper Container' "
        return paper

    def __fill_ink_in_pencil(self):
        if self.__ink_on_pencil < 10:
            if self.ink_storage > 10:
                self.__ink_on_pencil += 10
                self.ink_storage -= 10
                print("Filled Ink on Pincel")
            else:
                raise Exception("Ink Not Available")

    def __move_pencil(self, x=0, y=0, init=False):
        if not init:
            print(f"Pencil Moved to x:{x} and y:{y}")
        else:
            print("Pencil Moved to the Initial Position")

    def __print(self, file):
        coords = [[i, i * 2] for i in range(25)]

        for x, y in coords:
            self.__move_pencil(x, y)
            print("Printed")

            self.__ink_on_pencil -= 2
            self.__fill_ink_in_pencil()

        print("Finished Printing")

    def __throw_paper (self):
        print("Throwing the Paper")

if __name__ == "__main__":
    my_printer = Printer(20000)
    my_printer.print_file("perro")