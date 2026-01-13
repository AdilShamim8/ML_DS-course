class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in.")  # 'self' is the object

u = User("Alice")
u.login()
# Python secretly calls: User.login(u)