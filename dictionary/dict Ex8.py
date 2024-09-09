dict1={
    "name":"kelly",
    "age":"25",
    "salary": 8000,
    "city": "new york"
    }

if('city' in dict1):
    dict1['location']=dict1.pop('city')
print(dict1)
