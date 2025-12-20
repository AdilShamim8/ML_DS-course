while True:
    user_input = input("Enter your age: ")
    try: 
        age = int(user_input)
        print(f"Your age is {age}")
        break  
        
    except ValueError:
        print("Numbers only! Please try again.\n")