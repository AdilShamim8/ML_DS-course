user = None
if user is not None and user.get("role") == "admin":
    print("Access Granted:  Admin privileges activated")
else:
    print("Access Denied")

user = {"name": "Adil", "role": "admin"}

if user is not None and user.get("role") == "admin":
    print("Access Granted: Admin privileges activated")
else:
    print("Access Denied")