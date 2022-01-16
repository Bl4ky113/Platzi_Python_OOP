import time
import random
from typing import Iterator

def merge_sort (unorganized_list, iterarions=0):
    if len(unorganized_list) > 1:
        mid_point = len(unorganized_list) // 2
        left_list = unorganized_list[:mid_point]
        right_list = unorganized_list[mid_point:]

        merge_sort(left_list)
        merge_sort(right_list)

        left_iterator = 0
        right_iterator = 0
        main_iterator = 0

        while left_iterator < len(left_list) and right_iterator < len(right_list):
            if left_list[left_iterator] < right_list[right_iterator]:
                unorganized_list[main_iterator] = left_list[left_iterator]
                left_iterator += 1
            else:
                unorganized_list[main_iterator] = right_list[right_iterator]
                right_iterator += 1

            main_iterator += 1
            iterarions += 1

        while left_iterator < len(left_list):
            unorganized_list[main_iterator] = left_list[left_iterator]
            left_iterator += 1
            main_iterator += 1
            iterarions += 1

        while right_iterator < len(right_list):
            unorganized_list[main_iterator] = right_list[right_iterator]
            right_iterator += 1
            main_iterator += 1
            iterarions += 1

    return (unorganized_list, iterarions)

if __name__ == "__main__":
    size_list = int(input("Enter the Size of the List:  "))
    
    random_list = [random.randint(1, 100) for i in range(size_list)]
    print(f"List: \n{random_list}")
    print("-" * 10)

    start_time = time.time()
    (organized_list, iterations) = merge_sort(random_list)
    end_time = time.time()

    print(f"Organized List: \n{organized_list} in {iterations} iterations, in {end_time - start_time} secconds")