import time 

n = 1000000
large_list = list(range(n))
large_set = set(range(n))

search_for = -1

# Time list search
start = time.perf_counter()
result_list = search_for in large_list
list_time = time.perf_counter() - start

# Time set search  
start = time.perf_counter()
result_set = search_for in large_set
set_time = time.perf_counter() - start

print(f"Searching for {search_for} in {n:,} items:\n")
print(f"  List search: {list_time:.6f} seconds")
print(f"  Set search:   {set_time:.6f} seconds")
print(f"\n  Speedup:  {list_time/set_time: ,.0f}x faster!")