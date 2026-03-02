from itertools import groupby

data = [
    {"name":"A", "cat":"x"},
    {"name":"B", "cat":"x"},
    {"name":"C", "cat":"y"},
]
data.sort(key=lambda x: x["cat"])
for cat, items in groupby(data, key=lambda x: x["cat"]):
    print(cat, list(items))
# Output:
# x [{'name': 'A', 'cat': 'x'}, {'name': 'B', 'cat': 'x'}]
# y [{'name': 'C', 'cat': 'y'}]