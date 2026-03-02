# Day 5 Dictionaries (Hash Maps)

### 📖 DEEP DIVE: Theory: Hash Tables

A Dictionary is a Key-Value store. It is optimized for **O(1) Lookup**.
When you search a List, Python scans left-to-right (O(N)). When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in memory. It is instant, even with 1 million items.

```python
user = {"id": 1, "name": "Admin"}

# Safe Access (.get)
# Returns None if key missing, prevents crash
email = user.get("email", "No Email Found")

# Iteration
for key, val in user.items():
    print(f"{key}: {val}")
```

### 📖 DEEP DIVE: Micro-Challenge: The Speed Trap (Lookup)

**Goal:** Create a list of 1 million numbers. Create a set (hash table) of the same numbers. Check if the number -1 exists in both.

**Constraint:** You don't need to actually run 1M items, but explain why the Set/Dict is faster.

**The Mechanics:**

  * **List Search (O(N)):** Python must scan item 1, item 2, item 3... until the end.
  * **Dict/Set Search (O(1)):** Python runs `hash(-1)`, gets a memory address (e.g., 0x99), and looks *only* at that spot. It is instant.

---

### 📖 DEEP DIVE: Micro-Challenge: The Safe Vault

**Goal:** Create a dictionary `user = {"id": 1}`. Try to access `user["email"]`. Then try to access it safely.
**Constraint:** Use `.get()`.
**The Mechanics:** Direct access `user["key"]` raises a `KeyError` if the key is missing, crashing the script. The method `user.get("key", "Default")` checks the Hash Table. If the bucket is empty, it returns your default value (or None) instead of raising an error signal.

---

### 📖 DEEP DIVE: Micro-Challenge: The Frequency Counter

**Goal:** Input a string "banana". Create a dictionary that counts the frequency of each letter (e.g., `{'b':1, 'a':3, 'n':2}`).
**Constraint:** Use a standard `for` loop and `if/else` logic.
**The Mechanics:** This demonstrates **Dynamic Key Insertion**. As you loop through 'b', 'a', 'n', Python calculates the hash for each char.

* If the hash address is empty → Create Key, Value = 1.
* If the hash address is occupied → Value += 1.

---

### 📖 DEEP DIVE: Micro-Challenge: The Database Merger

**Goal:** You have two dictionaries: `defaults = {"theme": "light", "audio": "on"}` and `user_pref = {"theme": "dark"}`. Merge them so `user_pref` overrides defaults.
**Constraint:** Use the update operator `|` (Python 3.9+) or `.update()`.
**The Mechanics:** When merging, Python iterates through the second dictionary. It calculates the hash of "theme". It finds that "theme" already exists in the first dictionary's memory block, so it **Overwrites** the value. It finds "audio" is missing in the second, so it keeps the original.

