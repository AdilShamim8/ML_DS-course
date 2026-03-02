# Day 7 Error Handling (Exceptions)

## 📖 DEEP DIVE: Theory: Exception Bubbling

> When an error occurs, it "bubbles up" the call stack. If nothing catches it, the program crashes.
>
> **Defensive Programming:** We use `try/except` blocks to catch these bubbles. This is required for Data Science pipelines where one bad row of data shouldn't stop a 10-hour training process.

```python
while True:
    try:
        val = int(input("Enter number: "))
        print(100 / val)
        break
    except ValueError:
        print("Text is not allowed.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
```

## 📖 DEEP DIVE: Micro-Challenge: The Input Guard

> **Goal:** Write a script that asks the user for their age. If they type text (e.g., "twenty"), print "Numbers only" instead of crashing.
>
> **Constraint:** Use `try/except ValueError`.
>
> **The Mechanics:** When `int("text")` fails, Python raises a **Signal**. Normally, this signal bubbles up and kills the program. The `try` block creates a "Safety Net." If a specific signal (`ValueError`) hits the net, the interpreter jumps immediately to the `except` block, skipping any remaining code in the `try` section.

---

## 📖 DEEP DIVE: Micro-Challenge: The Math Safety Net

> **Goal:** create a variable `x = 0`. Try to print `100 / x`. Catch the specific error that occurs.
>
> **The Mechanics:** Division by zero is mathematically undefined. At the CPU level, the ALU (Arithmetic Logic Unit) throws a hardware interrupt. Python wraps this into a `ZeroDivisionError` object. Catching this allows your data pipeline to say "Skipping bad row" instead of halting a 10-hour process.

## 📖 DEEP DIVE: Micro-Challenge: The Cleanup Crew

> **Goal:** Write a `try/except` block that divides two numbers. Add a `finally` block that prints "Execution Complete" regardless of whether the division succeeded or failed.
>
> **The Mechanics:** The `finally` block is guaranteed to run. Even if the program crashes or returns early in the `try`, Python ensures the `finally` code executes before leaving the scope. This is critical for **Resource Management** (closing files, database connections, or network sockets) to prevent memory leaks.

## 📖 DEEP DIVE: Micro-Challenge: The Custom Signal

> **Goal:** Ask the user for a number. If the number is negative, manually trigger an error using `raise ValueError("No negatives")`.
>
> **The Mechanics:** You can enforce your own logic rules by "raising" exceptions manually. When you write `raise`, you are constructing an Exception Object and handing it to the Python interpreter, forcing it to stop normal execution and look for an exception handler (just like a built-in error).