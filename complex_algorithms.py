import time, sys


def factorial_normal (num):
    answer = 1
    
    while num > 1:
        answer *= num
        num -= 1

    return answer

def factorial_recursive (num):
    if num == 1:
        return 1

    return num * factorial_recursive(num - 1)

if __name__ == "__main__":
    num_factorial = 1000
    sys.setrecursionlimit(999999999)

    start_time = time.time()
    print(factorial_normal(num_factorial)) 
    stop_time = time.time()
    print(f"Time Normal: {stop_time - start_time}")
    
    start_time = time.time()
    print(factorial_recursive(num_factorial))
    stop_time = time.time()
    print(f"Time Recursive: {stop_time - start_time}")