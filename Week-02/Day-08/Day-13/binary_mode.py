# Read image file in binary
with open("cat.jpg", "rb") as img:
    raw_bytes = img.read()
    print(type(raw_bytes))  # <class 'bytes'>