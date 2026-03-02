class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name):
        super().__init__(name)   # Call parent __init__
        self.role = "Admin"

a = Admin("superuser")
print(a.name)   # "superuser"
print(a.role)   # "Admin"