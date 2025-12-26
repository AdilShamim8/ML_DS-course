def find_duplicates(list_A, list_B):
    matches = []

    for item_A in list_A:       # Outer Loop (Runs N times)
        for item_B in list_B:   # Inner Loop (Runs N times)

            # This comparison happens N * N times
            if item_A == item_B:
                matches.append(item_A)

    return matches

print(find_duplicates([1, 2, 3], [3, 4, 5]))



# import time
# A = list(range(10_000))
# B = list(range(5_000, 15_000))  # 5,000 overlaps

# start = time.perf_counter()
# dupes = []
# for a in A:
#     for b in B:
#         if a == b:
#             dupes.append(a)
# elapsed = time.perf_counter() - start

# print(f"Nested loops O(N²): Found {len(dupes)} duplicates in {elapsed:.4f} s")

# # Efficient O(N) way:
# start = time.perf_counter()
# setB = set(B)
# dupes_fast = [a for a in A if a in setB]
# elapsed_fast = time.perf_counter() - start
# print(f"Set-lookup O(N): Found {len(dupes_fast)} in {elapsed_fast:.4f} s")