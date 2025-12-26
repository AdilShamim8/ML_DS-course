def is_even(num):
    return num % 2 == 0

# Test cases
test_numbers = [0, 1, 2, 3, 4, 5, 100, -2, -3]

for n in test_numbers: 
    result = is_even(n)
    print(f"is_even({n}) {result}")