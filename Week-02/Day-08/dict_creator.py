def build_dict_from_list(lst):
    new_dict = {}

    for item in lst:  # Loop runs N times
        new_dict[item] = True

    return new_dict

print(build_dict_from_list([1, 2, 3, 4, 5]))


# import time

# lst = list(range(1_000_000))
# start = time.perf_counter()
# d = {x: True for x in lst}        # O(N) creation
# elapsed_create = time.perf_counter() - start

# start = time.perf_counter()
# found = 123456 in d               # O(1) lookup
# elapsed_lookup = time.perf_counter() - start

# print(f"Dict creation O(N): {elapsed_create:.6f} s")
# print(f"Dict lookup O(1): {elapsed_lookup:.8f} s")