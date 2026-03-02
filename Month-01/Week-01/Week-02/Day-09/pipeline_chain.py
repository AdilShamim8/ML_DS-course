def squares(nums):
    for x in nums:
        yield x*x

def filter_evens(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x

nums = range(10)
pipeline = filter_evens(squares(nums))  # Only even squares

print(list(pipeline))   # [0, 4, 16, 36, 64]