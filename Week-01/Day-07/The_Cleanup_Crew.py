def divide_with_cleanup(a, b):
    try:
        print(f"Attempting: {a} / {b}")
        result = a / b
        print(f"Result: {result}")
        return result
        
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
        
    finally:
        print("[FINALLY] Execution Complete")

print("Test 1: Successful division")
divide_with_cleanup(100, 5)

print("\nTest 2: Division by zero")
divide_with_cleanup(100, 0)