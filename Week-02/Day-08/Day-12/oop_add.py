class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return Wallet(self.balance + other.balance)

    def __repr__(self):
        return f"Wallet({self.balance})"

w1 = Wallet(100)
w2 = Wallet(150)
w3 = w1 + w2
print(w3)   # Wallet(250)