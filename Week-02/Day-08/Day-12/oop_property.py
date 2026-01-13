import datetime

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year

u = User("Dana", 2000)
print(u.age)    # Computed dynamically!