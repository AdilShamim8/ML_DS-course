word = "banana"

freq = {}

# Count each character
for char in word:
    if char in freq: 
        freq[char] += 1
    else:
        freq[char] = 1

print(f"\nFinal count: {freq}")