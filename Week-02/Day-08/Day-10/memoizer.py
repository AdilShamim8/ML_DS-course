def cache(func):
    saved = {}
    def inner(arg):
        if arg in saved:
            print(f"Cache hit for {arg}")
            return saved[arg]
        print(f"Cache miss for {arg}")
        result = func(arg)
        saved[arg] = result
        return result
    return inner

@cache
def slow_fib(n):
    if n < 2:
        return n
    return slow_fib(n-1) + slow_fib(n-2)

print(slow_fib(10))
print(slow_fib(8))  # Fast from cache!