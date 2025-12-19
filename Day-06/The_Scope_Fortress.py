x = 10

def change_x():
    x = 20
    print(f"Inside change_x(), x = {x}")

print(f"Before change_x(), x = {x}")
change_x()
print(f"After change_x(), x = {x}")