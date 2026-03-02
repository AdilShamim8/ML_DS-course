def calculate_hash(value):
    # Simple hash function for demonstration (use Python's built-in hash in practice)
    return hash(value)

def set_contains(set_obj, target):
    # step 1: Compute mathematical signature 
    hash_value = calculate_hash(target)

    # Step 2: Calculate memory address 
    bucket_index = hash_value % set_obj.total_buckets

    # step 3: Direct jump 
    Memory_slot = set_obj.buckets[bucket_index]

    if target in Memory_slot:
        return True
    return False


# import time

# data = list(range(10_000_000))
# data_set = set(data)               

# start = time.perf_counter()
# found = -5 in data_set            
# elapsed = time.perf_counter() - start

# print(f"Hash lookup: Is -5 in data_set? {found}")
# print(f"Time elapsed: {elapsed:.8f} seconds")
# # Complexity: O(1). Lookup time does NOT scale with size!