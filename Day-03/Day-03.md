# Day 3 Loops Iteration

### 📖 DEEP DIVE: Theory: The Iterator Protocol

Loops allow us to automate tasks.
* **For Loops:** Iterate over a known collection (List, String, Range).
* **While Loops:** Iterate as long as a condition (State) is True.

> **Warning:** While loops can run forever (Infinite Loop) if you don't write a line of code that changes the condition to False.

---

```python
# The Infinite Input Pattern
while True:
    pwd = input("Set Password (min 5 chars): ")
    if len(pwd) >= 5:
        print("Password Set")
        break # Exits the loop
    print("Too short. Try again.")
```

-----

### 📖 DEEP DIVE: Micro-Challenge: The Infinite Guardian

**Goal:** Write a script that asks the user for a password repeatedly. It must run forever until the user types "stop".

**Constraint:** Use `while True` and handle the exit condition manually.

**The Mechanics:** A `while True` loop creates an **Infinite Cycle** at the CPU level. The program pointer jumps back to the start of the block indefinitely. The `break` keyword is the only "Emergency Brake." It sends a signal to the interpreter to immediately terminate the current loop scope and jump to the next line of code outside the loop.

---

### 📖 DEEP DIVE: Micro-Challenge: The Accumulator Pattern

**Goal:** Ask the user for a number $N$ (e.g., 5). Calculate the sum of all numbers from 1 to $N$ ($1+2+3+4+5$).
**Constraint:** Do not use the math formula $\frac{n(n+1)}{2}$. You must use a `for` loop and a tracker variable.
**The Mechanics:** This teaches **State Retention**. Inside the loop, the variable `total` persists across iterations.

* Iteration 1: `total` becomes $0 + 1$.
* Iteration 2: `total` becomes $1 + 2$.

This is the foundational logic for complex algorithms like Neural Network training (updating weights).

---

### 📖 DEEP DIVE: Micro-Challenge: The Efficient Skipper

**Goal:** Loop through numbers 1 to 10. Print them, BUT if the number is 5, skip it and do not print anything.
**Constraint:** Use the `continue` keyword.
**The Mechanics:** `continue` forces a **Short-Circuit** of the current iteration. Unlike `break` (which kills the loop), `continue` tells the interpreter: "Ignore the rest of the code in this block, jump back to the top, and load the next item." This is crucial for filtering data streams without stopping the pipeline.

---

### 📖 DEEP DIVE: Micro-Challenge: The String Walker

**Goal:** Create a string `word = "DATA"`. Write a loop that prints every letter on a new line.
**The Mechanics:** This demonstrates the **Iterator Protocol**. Python strings are "Iterables". When you write `for char in word`, Python secretly calls `iter(word)`. It then calls `next()` repeatedly to fetch 'D', then 'A', then 'T', then 'A', until the string raises a `StopIteration` signal.

