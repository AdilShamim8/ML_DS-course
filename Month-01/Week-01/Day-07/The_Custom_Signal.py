def get_positive_number():
    while True:
        try:
            user_input = input("Enter a positive number: ")
            number = float(user_input)
            if number < 0:
                raise ValueError("No negatives allowed!")
            
            if number == 0:
                raise ValueError("Zero is not positive!")
            
            print(f"Accepted: {number}")
            return number
            
        except ValueError as e:
            print(f"Error: {e}\n")

result = get_positive_number()
print(f"\nFinal result: {result}")