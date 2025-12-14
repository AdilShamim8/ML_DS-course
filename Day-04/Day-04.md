# Day 4 Lists (Data Structures I)

## 📖 DEEP DIVE: Theory: Mutability Memory

Lists are **Mutable**. This means they can be changed in place.
**The Aliasing Trap:** `A = [1,2]` `B = A` This does NOT copy the list. It creates a second name for the same list. Modifying B will destroy A. **Solution:** Always use `B = A.copy()`.

---

```python
data = [10, 20, 30, 40, 50]

# Slicing (Start:Stop:Step)
subset = data[1:4] # [20, 30, 40]
reverse = data[::-1] # [50, 40, 30, 20, 10]

# List Comprehension
# [Action for Item in List if Condition]
squares = [x**2 for x in data]
```

---

## 📖 DEEP DIVE: Micro-Challenge: The Reference Trap

**Goal:** Create a list a = [1, 2, 3]. Set b = a. Change the first item of b to 99. Print a.

**Observation:** a also changes to [99, 2, 3]

**The Mechanics:** Lists are "Mutable Objects". When you write b = a, you are copying the Reference (Memory Address), not the data. Both a and b point to the exact same memory block.

Fix: Use b = a.copy() or b = a[:] to force Python to allocate a new list in memory.

---

## 📖 DEEP DIVE: Micro-Challenge: The Slicing Surgeon

**Goal:** Create a list `data = [10, 20, 30, 40, 50]`. Create a new list containing the last 3 items in reverse order.

**Constraint:** Use Slicing syntax `[start:stop:step]`

**The Mechanics:** The syntax `data[-1:-4:-1]` or `data[:1:-1]` creates a **Shallow Copy**. Unlike simple assignment, slicing tells the interpreter: "Go to this memory block, read these specific values, and build a **New Object** to hold them." This leaves the original list untouched.

---

## 📖 DEEP DIVE: Micro-Challenge: The Stack Emulator

**Goal:** Create an empty list. Add numbers 1, 2, 3. Then remove the last number (3) and print it.

**Constraint:** Use `.append()` and `.pop()`. Do not use `.insert()` or `.remove()`.

**The Mechanics:** This mimics a **LIFO (Last-In, First-Out) Stack**.

* `.append()` and `.pop()` are optimized to $O(1)$ time complexity because Python lists are "Dynamic Arrays." Adding/removing from the end is instant.
* `.insert(0, x)` is $O(N)$ because Python must shift every other item in memory to make room.

---

## 📖 DEEP DIVE: Micro-Challenge: The One-Line Architect

**Goal:** Create a list of numbers from 1 to 10. Generate a new list containing the **Squares** of only the **Even** numbers.

**Constraint:** Do this in exactly **one line** using List Comprehension.

**The Mechanics:**
Code: `[x**2 for x in nums if x % 2 == 0]`

List Comprehensions are not just syntactic sugar; they are faster than standard `for` loops. They are optimized at the C-level, avoiding the overhead of the Python interpreter constantly appending to a list.