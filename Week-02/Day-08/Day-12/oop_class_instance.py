class User:
    species = "Human"  # Shared by all users

    def __init__(self, name):
        self.name = name    # Unique to instance

u1 = User("A")
u2 = User("B")

print(u1.species)  # "Human"
print(u2.species)  # "Human"

User.species = "Alien"
print(u1.species)  # "Alien"
print(u2.species)  # "Alien"

u1.species = "Robot"
print(u1.species)  # "Robot"   [only u1]
print(u2.species)  # "Alien"   [still class-level for others]