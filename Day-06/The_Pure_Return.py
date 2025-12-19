# Function that prints but returns nothing
def add(a, b):
    result = a + b
    print(f"(Inside function) Sum: {result}")

res = add(5, 5)
print(f"(Outside function) Returned value: {res}")