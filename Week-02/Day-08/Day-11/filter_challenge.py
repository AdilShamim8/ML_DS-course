numbers = [-2, -1, 0, 1, 2, 3]
# Keep only positive numbers
positives = list(filter(lambda x: x >= 0, numbers))
print(positives) # [0, 1, 2, 3]

# Remove all falsy values (None, 0, "", etc.)
mixed = [0, "hi", "", None, 3]
cleaned = list(filter(None, mixed))
print(cleaned) # ["hi", 3]