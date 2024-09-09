dict1={
    "name":"kelly",
    "age": 25,
    "salary": 8000,
    "city": "new york"
    }
keys=["name","salary"]

for key in keys:
    dict1.pop(key, None)
print(dict1)

