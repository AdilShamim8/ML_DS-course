import json

data = {"a": 1, "b": 2}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Loading JSON back
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)