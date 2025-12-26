user = {"id": 1, "name":  "Admin"}


print("1. Direct access (unsafe):")
print(f"   user['id'] → {user['id']}")  


print("2. Safe access with .get():")

# Returns None if missing
email = user.get("email")
print(f"user. get('email') {email}")  