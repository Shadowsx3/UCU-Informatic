from time import time


def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """

    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret

    return wrapper
@count_elapsed_time
def test():
    for i in range(2, 10001):
        suma = 1
        for j in range(2, i):
            if i % j == 0:
                suma += j
                if suma > i:
                    break
        if i == suma:
            print(f'{i} es un numero perfecto')

test()

