import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return inner

@timer
def slow_square(n):
    time.sleep(0.5)
    return n ** 2

print(slow_square(8))