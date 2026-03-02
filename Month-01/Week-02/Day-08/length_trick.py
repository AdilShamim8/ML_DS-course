# def pylistobjext:
#        int ob_size
#        ptr *items
# FUNCTION get_length(list_obj):
#       return list_obj.ob_size




big_lst = list(range(1_000_000_000))  # 1 billion

import time
start = time.perf_counter()
n = len(big_lst)
elapsed = time.perf_counter() - start

print(f"len(big_lst): {n} items (Time: {elapsed:.8f} s)")
# Complexity: O(1) - len() is instant due to internal metadata.