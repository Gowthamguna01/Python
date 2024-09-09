employees=['kelly','emma','john']
defaults={"designation":'Application Developer','salary':8000}

dict1={employee:defaults.copy() for employee in employees}
print(dict1)
