import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    people = list(reader)
print(people)
# [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]