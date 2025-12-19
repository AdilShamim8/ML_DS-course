def connect(port=3306):
    print(f"Connecting to: {port}...")

# Call 1: Use all defaults
print("Call 1: connect()")
connect()

# Call 2: Override port only
print("\nCall 2: connect(port=5432)")
connect(port=5432)