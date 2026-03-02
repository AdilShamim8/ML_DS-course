def wrapper(func):
    def inner(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return inner

@wrapper
def add(a, b):
    return a + b

print(add(2, 3))  # ✅ Prints 5