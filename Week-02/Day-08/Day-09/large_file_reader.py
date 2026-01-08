def fake_file_reader(n):
    """Yield n fake lines as if reading a huge file."""
    for i in range(n):
        yield f"line {i+1}"

print("Reading big file:")
for i, line in enumerate(fake_file_reader(100_000_000)):
    if i < 3 or i > 99_999_996:
        print(line)
    if i == 5:
        print("...")
    if i > 6 and i < 99_999_997:
        continue
    if i >= 10:  # Just demo start/end!
        break