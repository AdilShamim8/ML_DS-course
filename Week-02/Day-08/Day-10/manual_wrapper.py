def wrapper(func):
    def inner():
        print("Before call")
        func()
        print("After call")
    return inner

def hello():
    print("Hello world!")

new_func = wrapper(hello)
new_func()  # Output: Before call, Hello world!, After call