class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

class Admin(User):            # Inherits User
    def delete_db(self):
        print("DB deleted!")

a = Admin("root")
a.greet()         # Inherited!
a.delete_db()     # Only admin