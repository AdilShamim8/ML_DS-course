def add_char(old_string, char):
    old_size = len(old_string)
    new_size = old_size + 1

    # Step 1: Allocate NEW memory block
    new_memory = [''] * new_size

    # Step 2: Copy ALL characters from old to new
    for i in range(old_size):
        new_memory[i] = old_string[i]

    # Step 3: Add the new character
    new_memory[old_size] = char

    # No need to free memory in Python
    return ''.join(new_memory)

print(add_char("hello", '!')) 



# import time

# N = 10_000
# s = ""
# start = time.perf_counter()
# for _ in range(N):
#     s += "a"      # Each += allocates a NEW string (O(N²) total)
# elapsed_bad = time.perf_counter() - start

# # Efficient way:
# start = time.perf_counter()
# chars = ["a"] * N
# s2 = "".join(chars)   # Allocates ONCE, O(N)
# elapsed_good = time.perf_counter() - start

# print(f"s += 'a' (O(N²)): {elapsed_bad:.6f} s")
# print(f"''.join() (O(N)): {elapsed_good:.6f} s")