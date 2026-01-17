# Append (no data loss)
with open("log.txt", "a") as f:
    f.write("Log entry added\n")

# Overwrite (delete everything, start fresh)
with open("log.txt", "w") as f:
    f.write("Fresh log entry\n")

# Safety: 'x' mode fails if file exists
try:
    with open("log.txt", "x") as f:
        f.write("Should only work once!\n")
except FileExistsError:
    print("File already exists, 'x' mode prevents overwrites.")