class User:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

u1 = User(1)
u2 = User(1)
u3 = User(2)
print(u1 == u2)  # True
print(u1 == u3)  # False