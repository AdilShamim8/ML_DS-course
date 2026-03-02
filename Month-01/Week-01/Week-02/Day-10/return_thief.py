def wrapper(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)  # Forgot to return result!
    return inner

@wrapper
def give(x):
    return x * 2

result = give(10)
print(result)  # None (Value was lost!)

# ➡️ THE FIX: return func(*args, **kwargs)
