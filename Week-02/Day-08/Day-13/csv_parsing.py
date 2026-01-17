import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    people = list(reader)
print(people)

# [{'name': 'Adil', 'age': '21'}, {'name': 'Harry', 'age': '25'}]
