def merge_sort(list):
    if len(list) <= 1:
        return list
    left = merge_sort(list[0:len(list)//2])
    right = merge_sort(list[len(list)//2:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# import random, time

# lst = random.sample(range(1_000_000), 1_000_000)
# start = time.perf_counter()
# lst.sort()  # Timsort: O(N log N)
# elapsed = time.perf_counter() - start

# print(f"Sorting 1 million items took {elapsed:.4f} seconds")
# # Avoid sorting inside loops!