def pop_from_start(lst):
    target = lst[0]
    N = len(lst)

    # Start from 0, pull everyone one step left
    for i in range(0, N-1):
        lst[i] = lst[i+1]  # The Shift Operation

    del lst[-1]
    return target

print(pop_from_start(list(range(10))))  




# import time

# N = 1000000
# lst = list(range(N))

# # .pop() from end (O(1))
# start = time.perf_counter()
# lst.pop()
# end_pop_time = time.perf_counter() - start

# # .pop(0) from front (O(N))
# start = time.perf_counter()
# lst.pop(0)
# start_pop_time = time.perf_counter() - start

# print(f"pop() from end: O(1) - Time: {end_pop_time:.8f} sec")
# print(f"pop(0) from start: O(N) - Time: {start_pop_time:.8f} sec")

# # Fix: Use collections.deque for fast FIFO!
# from collections import deque
# dq = deque(range(N))

# start = time.perf_counter()
# dq.popleft()
# deque_time = time.perf_counter() - start
# print(f"deque.popleft(): O(1) - Time: {deque_time:.8f} sec")