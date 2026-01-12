tuples = [(1, 2), (3, 4)]

# This will fail: tuples in Python are immutable!
def try_modify(t):
    try:
        t[0] = 99
    except TypeError as e:
        return str(e)
    return t

results = list(map(try_modify, tuples))
print(results)  # ["'tuple' object does not support item assignment", ...]

# Functional style: return a new tuple
def plus_one(t):
    # Returns a NEW tuple (does not mutate input)
    return (t[0] + 1, t[1] + 1)

print(list(map(plus_one, tuples)))  # [(2, 3), (4, 5)]