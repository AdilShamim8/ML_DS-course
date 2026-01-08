def gen():
    yield from [1,2,3]

g = gen()
print("First loop:")
for x in g:
    print(x)

print("Second loop (should not print anything):")
for x in g:
    print(x)