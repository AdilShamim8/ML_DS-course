# Day 1: The Environment & Building Blocks

## 📖 DEEP DIVE: Theory: The Python Memory Model

To become a Data Scientist, you must understand how Python manages memory. It is distinct from C or Java.

1. **Everything is an Object:** Numbers, Strings, and Lists are all objects stored in Heap Memory.
2. **Variables are References (Sticky Notes):** When you execute `x = 10`:
    1. Python creates an object `int(10)` at memory address `0x7ff....`
    2. Python creates the name `x`.
    3. Python draws a line (reference) connecting `x` to `0x7ff....`
3. **Garbage Collection:** Python uses "Reference Counting". If you delete `x`, the reference count for object `10` drops to 0. Python’s Garbage Collector then instantly destroys the object to free up RAM.

---

## Syntax Spotlight: The Safe Input Pattern

```python
# Standard Input (Unsafe)
# age = input("Age: ") <-- Returns "25" (String)

# The Academy Standard (Safe)
raw_val = input("Enter Principal: ")
try:
    principal = float(raw_val) # Explicit Casting
    print(f"Accepted: ${principal:,.2f}") # F-String Formatting
except ValueError:

    print("Error: Invalid Number")


## 📖 DEEP DIVE: Micro-Challenge: The Identity Swap

**Goal:** Initialize `x = 100` and `y = 200`. Swap their values so `x` becomes 200 and `y` becomes 100.

**Constraint:** You must do this in **exactly one line of code**. Do not use a temporary variable (e.g., `temp = x`).

**The Mechanics:** In C++ or Java, this is impossible without a temp variable. In Python, the syntax `x, y = y, x` works because:

1. The Right Side `y, x` creates a temporary **Tuple** object `(200, 100)` in the Heap.
2. The Left Side performs **Unpacking**, re-assigning the reference `x` to index 0 and `y` to index 1.
3. The temporary tuple is then Garbage Collected.

---

## 📖 DEEP DIVE: Micro-Challenge: The Type Auditor

**Goal:** Ask the user to type a number.

1. Print the `type()` of the raw input.
2. Cast it to a `float`.
3. Print the `type()` again.

**The Mechanics:** This drill proves that `input()` is strictly a string-fetcher. The "transformation" in Step 2 does not change the original object (Strings are immutable). The `float()` constructor allocates a **brand new object** at a different memory address.

---

## 📖 DEEP DIVE: Micro-Challenge: The Precision Banker

**Goal:** Create a variable `bill = 100 / 3`.

**Constraint:** Print the result formatted strictly to **3 decimal places** with a dollar sign (e.g., $33.333).

**The Mechanics:** Python floats use IEEE 754 double-precision (64-bit). The actual number in memory is 33.333333333333336. **F-Strings** act as a "View Layer," masking the raw precision for the user interface without altering the underlying data integrity.

