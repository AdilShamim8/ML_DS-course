from collections import Counter

def are_anagrams(a, b):
    return Counter(a) == Counter(b)

print(are_anagrams("silent", "listen"))  # True
print(are_anagrams("hello", "world"))    # False