import functools

def wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@wrapper
def my_func():
    """important docstring"""
    pass

print(my_func.__name__)       # "my_func"
print(my_func.__doc__)        # "important docstring"