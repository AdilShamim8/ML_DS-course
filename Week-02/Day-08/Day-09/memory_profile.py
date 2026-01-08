import sys

comp = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print("List comprehension size:", sys.getsizeof(comp), "bytes")  
print("Generator expression size:", sys.getsizeof(gen), "bytes") 