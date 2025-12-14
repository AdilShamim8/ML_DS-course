# > Day 2 Logic Control Flow

## 📖 DEEP DIVE: Theory: Boolean Algebra Short-Circuiting

Logic is the brain of your code.
**Truthiness:** In Python, the following are considered **False**: `0`, `0.0`, `""` (Empty String), `[]` (Empty List), `None`. **Everything else is True.**
**Short-Circuit Evaluation:** `if A and B`: If **A** is **False**, Python **never checks B**. This is critical for preventing crashes (e.g., checking if a variable exists before accessing it).

```python
score = 85

# The Efficient Ladder
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B" # Stops here if True.
else:
    grade = "C"

# Ternary Operator (One-line Logic)
status = "Pass" if score >= 70 else "Fail"
```

## 📖 DEEP DIVE: Micro-Challenge: The Guard Clause (Short-Circuiting)

**Goal:** Create a variable `user = None`. Write an `if` statement that checks if `user` is not `None` AND if `user` has "admin" access.
**Constraint:** You must perform both checks in a single line. It must **not** crash when `user` is `None`.
**The Mechanics:** Python uses **Short-Circuit Evaluation**.

  * In the expression `if A and B`: If **A** is **False**, the interpreter **never executes B**.
  * This acts as a "Guard," preventing the code from trying to access attributes of a `NoneType` object, which would cause an `AttributeError`.

---

# 📖 DEEP DIVE: Micro-Challenge: The Floating Point Trap

**Goal:** Write a script that checks if `0.1 + 0.2 == 0.3`. Print the result (True/False).
**Observation:** It prints `False`.
**The Mechanics:** Computers use binary (Base-2) to store numbers. Just as `1/3` cannot be represented perfectly in decimal (0.333...), `0.1` cannot be represented perfectly in binary. The actual sum in memory is `0.30000000000000004`. **Fix:** Always use a tolerance threshold (epsilon) or `round()` when comparing floats in Data Science.

---

# 📖 DEEP DIVE: Micro-Challenge: The Truthiness Inspector

**Goal:** Create a variable `data = []` (Empty List). Write an `if` statement to print "Data Found" or "No Data" without comparing it to anything (e.g., do not use `len(data) > 0`).
**The Mechanics:** Python objects have inherent Boolean values.

* **Falsy:** `0`, `0.0`, `None`, `False`, empty collections (`""`, `[]`, `{}`).
* **Truthy:** Everything else.

The interpreter implicitly calls `bool(data)` behind the scenes, making code cleaner and faster.

---

# 📖 DEEP DIVE: Micro-Challenge: The Ternary Packer

**Goal:** You have a variable `score = 85`. Assign a variable `status` to "Pass" if `score > 70` else "Fail".
**Constraint:** Do this in exactly **one line of code**.
**The Mechanics:** This is a **Conditional Expression**: `status = "Pass" if score > 70 else "Fail"` Unlike a standard `if/else` block which controls *flow*, this expression evaluates to a *value* that is immediately assigned to the variable stack. It is atomic and atomic operations are often slightly faster.