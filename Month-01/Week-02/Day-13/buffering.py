# OS and Python buffer I/O
with open("huge.txt", "w") as f:
    for i in range(1_000_000):
        f.write(f"Line {i}\n")
# Disk is NOT written to 1 million times; OS flushes buffer in chunks!