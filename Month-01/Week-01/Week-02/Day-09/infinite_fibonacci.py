def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Demo: Print the first 10 Fibonacci numbers
f = fib()
for _ in range(10):
    print(next(f), end=" ")