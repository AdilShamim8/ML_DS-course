# Day 6 Functions Modularity

## 📖 DEEP DIVE: Theory: The Stack Scope

When a function is called, Python creates a "Stack Frame" in memory. All variables created inside the function live there. When the function returns, the frame is destroyed.

**LEGB Rule:** Python searches for variables in this order: Local -> Enclosing -> Global -> Built-in.

---

### Code Example

```python
def calculate_area(radius: float) -> float:
    """Returns area of circle. Inputs float."""
    if radius < 0:
        return 0
    return 3.14 * (radius**2)

# Main Execution
r = 5
print(calculate_area(r))
```

----

## 📖 DEEP DIVE: Micro-Challenge: The Scope Fortress

**Goal:** Create a global variable `x = 10`. Write a function `change_x()` that sets `x = 20` inside it. Print `x` outside the function.

**Observation:** It prints 10, not 20.

**The Mechanics:** This demonstrates **Local vs. Global Scope**. When you write `x = 20` inside a function, Python creates a **new local variable** named 'x' inside the function's stack frame. It does NOT touch the global 'x'. To modify the global, you would need the `global` keyword (but avoid this in production\!).

---

## 📖 DEEP DIVE: Micro-Challenge: The Pure Return

**Goal:** Write a function `add(a, b)` that prints the sum but returns nothing. Assign the result to a variable `res = add(5, 5)`. Print `res`.

**Observation:** It prints `None`.

**The Mechanics:** Every Python function returns something. If you do not explicitly write `return value`, Python implicitly executes `return None` at the end. **Best Practice:** Functions should calculate and return values. The calling code should decide whether to print them.

---

## 📖 DEEP DIVE: Micro-Challenge: The Default Gateway

**Goal:** Write a function `connect(port=3306)` that prints "Connecting to [port]". Call it once with no arguments, and once with `5432`.

**The Mechanics:** This uses **Default Arguments**. When Python defines the function, it stores `3306` in memory. If the caller provides no argument, Python grabs this stored default. This allows for flexible APIs where common settings are optional.

---

## 📖 DEEP DIVE: Micro-Challenge: The Logic Gate

**Goal:** Write a function `is_even(num)` that returns `True` if even, `False` otherwise.

**Constraint:** Do not use `if/else`. Do it in one line.


**The Mechanics:** Code: `return num % 2 == 0` Comparison operators (like `==`) evaluate directly to a Boolean value. You don't need to check `if True return True`. You can simply return the result of the comparison itself.
