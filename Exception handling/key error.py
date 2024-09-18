try:
    sampledict={
        "name":"hari",
        "age":20
        }

    emp_name=sampledict['name']
    print(emp_name)
    emp_age=sampledict['year']
    print(emp_age)
except KeyError as k:
    print("key is not matched",k)
