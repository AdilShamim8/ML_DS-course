nums = [-3, 0, 5, 7]

any_negative = any(x < 0 for x in nums)
all_positive = all(x > 0 for x in nums)

print(f"Any negative: {any_negative}")   # True
print(f"All positive: {all_positive}")   # False