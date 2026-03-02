def wrapper(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

@wrapper
def greet():
    print("Hi!")

greet()
# Equivalent to: greet = wrapper(greet)