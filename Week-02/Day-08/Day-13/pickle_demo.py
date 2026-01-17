import pickle

class User:
    def __init__(self, name):
        self.name = name

alice = User("Alice")

# Save (pickle) to file
with open("user.pkl", "wb") as f:
    pickle.dump(alice, f)

# Load (unpickle) from file (WARNING: don't do this with untrusted files!)
with open("user.pkl", "rb") as f:
    loaded_user = pickle.load(f)
    print(loaded_user.name)