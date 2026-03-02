def repeat(times):
    def decorator(func):
        def inner(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return inner
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()