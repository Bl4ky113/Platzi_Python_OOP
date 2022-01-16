import random
import time

def buble_sort (sorting_list):
    num = len(sorting_list)
    sorted_list = sorting_list
    iterations = 0

    for i in range(num):
        print(sorted_list)
        for j in range(0, num - (i + 1)):
            iterations += 1
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            
    return (sorted_list, iterations)

if __name__ == "__main__":
    size_list = int(input("Enter the size of the List to Sort:  "))

    disorganized_list = [random.randint(0, 100) for i in range(size_list)]

    start_time = time.time()
    (organized_list, iterations) = buble_sort(disorganized_list)
    end_time = time.time()

    print(f"Disordered List: {disorganized_list}")
    print(f"Ordered List: {organized_list}, in {iterations} iterations on {end_time - start_time} secconds")

""" O(n)* * O(n)** = O(n * n) = O(n**2)
    * for i loop
    ** for j loop
"""