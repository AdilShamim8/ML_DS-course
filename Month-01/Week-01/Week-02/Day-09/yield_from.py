def genA():
    yield "A1"
    yield "A2"

def genB():
    yield "B1"
    yield "B2"

def combined():
    yield from genA()
    yield from genB()

for val in combined():
    print(val)
# Output: A1  A2  B1  B2