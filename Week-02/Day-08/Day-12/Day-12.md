# > Day 12: The Blueprint (OOP)

## 📖 DEEP DIVE: 12.1 Micro-Challenge: The Constructor

* **Goal:** Create a class `User`. Ensure every user starts with `is_active = True`.
* **Deep Dive:** The `__init__` method is the "Constructor". Python calls it automatically immediately after memory allocation to initialize the object's state.

---

## 📖 DEEP DIVE: 12.2 Micro-Challenge: The Self Reference

* **Goal:** Explain why `def method(self)` is required.
* **Deep Dive:** Python passes the instance object as the first argument automatically. `user.login()` → `User.login(user)`. Without `self`, the method doesn't know *which* user's data to access.

---

## 📖 DEEP DIVE: 12.3 Micro-Challenge: The String Representation

* **Goal:** Make `print(user)` show "User: [Name]" instead of memory address.
* **Deep Dive:** Override `__str__` (for end-users) and `__repr__` (for developers/debugging).

---

## 📖 DEEP DIVE: 12.4 Micro-Challenge: Private Variables

* **Goal:** Prevent external code from changing `user.password`.
* **Deep Dive:** Rename it to `__password`. Python performs **Name Mangling** (→ `_User__password`), making it harder (though not impossible) to access from outside.

---

## 📖 DEEP DIVE: 12.5 Micro-Challenge: The Property Decorator

* **Goal:** Create a "fake" variable `user.age` that is calculated from birth year when accessed.
* **Deep Dive:** Use `@property`. It looks like a variable access, but runs a method behind the scenes. This is **Encapsulation**.

---

## 📖 DEEP DIVE: 12.6 Micro-Challenge: Class Variables vs Instance Variables

* **Goal:** Set `species = "Human"` on the Class. Set `name = "A"` on the Instance. Change `species` and see who is affected.
* **Deep Dive:** Class Variables are shared by ALL instances (Memory Optimization). Instance variables are unique to the object.

---

## 📖 DEEP DIVE: 12.7 Micro-Challenge: Inheritance

* **Goal:** Create `Admin(User)`. Add a method `delete_db()` only for Admin.
* **Deep Dive:** The child class inherits all attributes of the parent. It checks its own namespace first, then the parent's. This follows the **MRO (Method Resolution Order)**.

---

## 📖 DEEP DIVE: 12.8 Micro-Challenge: The Super Proxy

* **Goal:** Override `__init__` in Admin, but still run the User setup.
* **Deep Dive:** Use `super().__init__()`. This calls the parent method, ensuring base initialization logic isn't lost.

---

## 📖 DEEP DIVE: 12.9 Micro-Challenge: Operator Overloading

* **Goal:** Allow adding two wallets: `w1 + w2`.
* **Deep Dive:** Define `__add__`. When Python sees `+`, it calls this method. This allows objects to behave like native types (Polymorphism).

---

## 📖 DEEP DIVE: 12.10 Micro-Challenge: Equality

* **Goal:** Make `User(1)` equal to another `User(1)`.
* **Deep Dive:** By default, `==` checks memory address (identity). Override `__eq__` to check content (value).