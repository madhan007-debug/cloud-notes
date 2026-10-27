import json

student = {"name": "Love", "day": 9, "tools": ["Linux", "Git", "Python"]}

with open("student.json", "w") as f:
    json.dump(student, f, indent=2)

with open("student.json") as f:
    data = json.load(f)

print(data["name"])
print(data["tools"][1])

text = json.dumps(data)
print(type(text))
back = json.loads(text)
print(type(back))
