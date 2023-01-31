import time
from functools import wraps


def timeit(func):
    print("@timeit")
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        print("@timeit_wrapper")
        print(*args, **kwargs)
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"FUnction- {func.__name__} executed. Time taken: {total_time:.4f} seconds")
        return result
    return timeit_wrapper


@timeit
def calc_factorial(num):
    """
    Function to calculate factorial of num
    """
    print("@ calc_factorial")
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(num):
            fact *= (i+1)
        print(f"@calc_factorial finished: {fact}")
        return fact


if __name__ == "__main__":
    # calc_factorial(0)
    # calc_factorial(1)
    calc_factorial(5)
