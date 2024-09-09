dict1={
    "name":"kelly",
    "age":25,
    "salary": 8000,
    "city":"New York"
    }


keys=["name","salary"]
dict2={key: dict1[key] for key in keys}
print(dict2)
