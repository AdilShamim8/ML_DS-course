def simple():
    yield 'a'
    yield 'b'

g = simple()

print("Calling next() manually:")

print(next(g))  # 'a'
print(next(g))  # 'b'
try:
    print(next(g))  # Should raise StopIteration
except StopIteration:
    print("StopIteration raised: generator is exhausted.")