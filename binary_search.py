import time

def binary_search (organized_arr, objective, start_search, end_search, iterations=0):
    iterations += 1
    middle_search = (end_search + start_search) // 2

    print(f"start: {start_search}, middle: {middle_search}, end: {end_search}")

    if start_search > end_search:
        return (False, iterations)

    if organized_arr[middle_search] == objective:
        return (True, iterations)
    elif organized_arr[middle_search] < objective:
        return binary_search(organized_arr, objective, middle_search + 1, end_search, iterations)
    else:
        return binary_search(organized_arr, objective, start_search, middle_search - 1, iterations)

if __name__ == "__main__":
    size_arr = int(input("Enter the size of the List:  "))
    objective = int(input("Enter the number to find:  "))

    random_arr = [i for i in range(size_arr + 1)]

    start_time = time.time()
    (result, iterations) = binary_search(random_arr, objective, 0, len(random_arr) -1)
    end_time = time.time()

    print(f"List: {random_arr}")
    print(f"The number was{'' if result else ' not'} found in {iterations} iterations and in {end_time - start_time} secconds")

""" O(n)
"""

