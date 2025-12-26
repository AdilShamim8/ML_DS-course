# Day 8: The Physics of Code (Time Complexity)

### 📖 DEEP DIVE: 8.1 Micro-Challenge: The Linear Scan (O(N))

**Goal:** Create a list of 10 million numbers. Check if `-5` is in the list.  
**Deep Dive:** Python performs a **Linear Search**. It loads index 0, compares, loads index 1, compares... all the way to 10 million. *Complexity:* $O(N)$. If data doubles, time doubles.

---

### 📖 DEEP DIVE: 8.2 Micro-Challenge: The Hash Lookup (O(1))

**Goal:** Convert that list to a `set`. Check for `-5` again.  
**Deep Dive:** Python runs `hash(-5)`, gets a memory address, and looks directly at that slot. It never scans the other items. *Complexity:* $O(1)$. Constant time, regardless of data size.

---

### 📖 DEEP DIVE: 8.3 Micro-Challenge: The Insertion Trap (O(N))

**Goal:** Compare `list.append(x)` vs `list.insert(0, x)`.  
**Deep Dive:** `.append()` puts data in the next empty memory slot ($O(1)$). `.insert(0, x)` forces Python to **shift** every single existing item one step to the right in memory to make room. *Result:* Inserting at the start of a large list is catastrophic for performance.

---

### 📖 DEEP DIVE: 8.4 Micro-Challenge: The Queue Bottleneck (Pop)

**Goal:** Compare `list.pop()` vs `list.pop(0)`.  
**Deep Dive:** `.pop()` removes the last item ($O(1)$). `.pop(0)` removes the first item, requiring a **Left Shift** of all remaining items to fill the gap ($O(N)$). *Fix:* Use `collections.deque` for fast First-In-First-Out queues.

---

### 📖 DEEP DIVE: 8.5 Micro-Challenge: The String Builder ($O(N^2)$)

**Goal:** Loop 10,000 times and add a character to a string using `s += "a"`.  
**Deep Dive:** Strings are **Immutable**. Every time you do `+=`, Python destroys the old string and creates a **brand new** larger one in a new memory address. *Fix:* Use `"".join(list_of_chars)`.

---

### 📖 DEEP DIVE: 8.6 Micro-Challenge: The Length Trick ($O(1)$)

**Goal:** Call `len()` on a list of 1 billion items.  
**Deep Dive:** You might expect Python to count items one by one. It doesn't. The C-structure of a Python list maintains a metadata counter `ob_size`. `len()` simply reads this cached integer. It is instant.

---

### 📖 DEEP DIVE: 8.7 Micro-Challenge: The Quadratic Nested Loop ($O(N^2)$)

**Goal:** Find duplicates between two lists using nested `for` loops.  
**Deep Dive:** For every item in List A, you scan all items in List B. $10,000 \times 10,000 = 100,000,000$ operations. This is **the most common cause** of server timeouts.

---

### 📖 DEEP DIVE: 8.8 Micro-Challenge: The Sorting Cost ($O(N \log N)$)

**Goal:** Sort a random list.  
**Deep Dive:** Python uses **Timsort** (a hybrid of Merge Sort and Insertion Sort). It is faster than $O(N^2)$ but slower than $O(N)$. Avoid sorting inside loops!

---

### 📖 DEEP DIVE: 8.9 Micro-Challenge: The Dictionary Creator ($O(N)$)

**Goal:** Measure the time to create a dict from a list vs searching it.  
**Deep Dive:** Searching is $O(1)$, but **building** the dictionary takes $O(N)$ because Python must calculate the hash for every single item and allocate memory buckets.

---

### 📖 DEEP DIVE: 8.10 Micro-Challenge: The Slice Copy ($O(k)$)

**Goal:** Slice a massive list `data[0:5000]`.  
**Deep Dive:** Slicing is not free. It allocates new memory and copies the data references. Slicing a huge chunk takes time proportional to the slice size ($k$).