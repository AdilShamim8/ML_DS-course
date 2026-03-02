def find_missing(nums, N):
    total = N * (N+1) // 2
    actual = sum(nums)
    return total - actual

N = 100
nums = list(range(1, N+1))
nums.remove(77)   # remove one
print(find_missing(nums, N))  # 77