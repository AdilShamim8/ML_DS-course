USER = "guest"

def admin_required(func):
    def inner(*args, **kwargs):
        if USER != "admin":
            raise PermissionError("Only admin allowed!")
        return func(*args, **kwargs)
    return inner

@admin_required
def secret():
    return "Classified info!"

try:
    print(secret())
except PermissionError as e:
    print(f"Access denied: {e}")

USER = "admin"
print(secret())  # Allowed for admin