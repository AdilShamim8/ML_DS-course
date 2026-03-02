class User:
    def __init__(self, name):
        self.name = name
        self.is_active = True  # All users start active

u = User("Alice")
print(u.is_active)  # True