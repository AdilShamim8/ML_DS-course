import time

nums = list(range(1_000_000))

start = time.time()
mapped = list(map(lambda x: x + 1, nums))
map_time = time.time() - start

start = time.time()
comp = [x + 1 for x in nums]
comp_time = time.time() - start

print(f"map+lambda: {map_time:.5f}s")
print(f"list comp:  {comp_time:.5f}s")
print(f"Speedup: {map_time / comp_time:.2f}x")