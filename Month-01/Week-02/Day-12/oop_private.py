class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password  # Private to class

u = User("Alice", "secret123")
# print(u.__password)         # Error!
print(u._User__password)      # "secret123" (name mangling workaround)