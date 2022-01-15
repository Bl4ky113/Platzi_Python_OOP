import random

def lineal_search (arr, objective, iteration=0):
    match = False

    for item in arr:
        iteration += 1
        if item == objective:
            match = True
            break

    return (match, iteration)

if __name__ == "__main__":
    size_arr = int(input("Enter the size of the List:  "))
    objective = int(input("Enter the number to find:  "))

    random_arr = [random.randint(objective * -1, objective * 2) for i in range(size_arr)]

    (result, iteration) = lineal_search(random_arr, objective)

    print(f"List: {random_arr}")
    print(f"The number was{'' if result else ' not'} found in {iteration} iterations")

""" O(n)* + O(n)** = O(2n) = O(n) 
    * Lineal Search Loop
    ** List Comprehesion for random_arr
"""
