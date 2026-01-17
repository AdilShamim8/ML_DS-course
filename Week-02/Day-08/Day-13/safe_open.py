# Safest way to open/write/close a file
with open("my_file.txt", "w") as f:
    f.write("Hello world!\n")
# File automatically closed even if error crashes block!