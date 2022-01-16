import time
import random

def insert_sort (unorganized_list):
    iterations = 0

    for i in range(1, len(unorganized_list)):
        actual_value = unorganized_list[i]
        actual_index = i

        while actual_index > 0 and actual_value < unorganized_list[actual_index - 1]:
            unorganized_list[actual_index] = unorganized_list[actual_index - 1]
            actual_index -= 1
            iterations += 1

        unorganized_list[actual_index] = actual_value

    return (unorganized_list, iterations)

if __name__ == "__main__":
    size_list = int(input("Enter the size of the List:  "))

    unorganized_list = [random.randint(1, 100) for i in range(size_list)]
    print(f"List: {unorganized_list}")

    start_time = time.time()
    (organized_list, iterations) = insert_sort(unorganized_list)
    end_time = time.time()

    print(f"Organized List: {organized_list} in {iterations} iterarions, in {end_time - start_time} secconds")

""" O(n)* * O(n)** = O(n ** 2)
    * For loop
    ** While Loop
"""