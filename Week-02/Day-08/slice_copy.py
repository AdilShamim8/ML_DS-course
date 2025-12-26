def slice_list(source, k):
    # Step 1: Allocate memory for k items
    new_list = [None] * k

    # Step 2: Copy values one by one
    for i in range(0, k):
        new_list[i] = source[i]

    return new_list
print(slice_list(list(range(10)), 5))



# import time

# N = 1_000_000
# data = list(range(N))

# start = time.perf_counter()
# chunk = data[0:5_000]  # Slicing allocates & copies k items
# elapsed = time.perf_counter() - start

# print(f"Slicing data[0:5000] (O(k)): {elapsed:.8f} s")
# # Proportional to slice size, not total list size