from random import randint

def generate_num_file (name="./num_file.txt", length=25, random_nums=[0, 100]):
    """ Generates a file with a range of random numbers, for using with python.

        name: path of the file,
        length: length (in lines) of the file,
        random_num: range of the randint function

        returns file with length of random numbers in random_num range
    """
    numbers_arr = [randint(random_nums[0], random_nums[1]) for i in range(length)]

    with open(name, "w+") as file:
        for number in numbers_arr:
            file.write(f"{number}\n")

if __name__ == "__main__":
    while True:
        try:
            name_file = input("Enter the Name (or path) of the File:  ")
            size_file = int(input("Enter the Length of the File:  "))
            
            if size_file <= 0:
                raise ValueError

            range_nums = []
            while len(range_nums) < 2:
                range_num = int(input(f"Enter the Range of the Numbers({'min' if len(range_nums) < 1 else 'max'}):  "))
                range_nums.append(range_num)

            print(range_nums)
            if range_nums[0] > range_nums[1]:
                raise ValueError

            generate_num_file(name_file, size_file, range_nums)
            break

        # except ValueError:
        #     print("Value Error on Input")
        except KeyboardInterrupt:
            break
        # except:
        #     print("Error on Input")
