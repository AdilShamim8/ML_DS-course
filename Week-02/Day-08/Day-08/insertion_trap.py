# def insert_at_zero(lst, new_value):
#     N = len(lst)

#     # Increase the list size by one to avoid IndexError
#     lst.append(None)
#     # Start from the end, move everyone one step to the right
#     for i in range(N, 0, -1):
#         lst[i] = lst[i - 1]

#     # Now index 0 is "empty" (overwritable)
#     lst[0] = new_value



import time

N = 1000000
lst = list(range(N))

# .append(x) at end
start = time.perf_counter()
lst.append(-123)
append_time = time.perf_counter() - start

# .insert(0, x) at start (forces memory shift)
start = time.perf_counter()
lst.insert(0, 999)
insert_time = time.perf_counter() - start

print(f"append: O(1) - Time: {append_time:.8f} sec")
print(f"insert(0, x): O(N) - Time: {insert_time:.8f} sec")