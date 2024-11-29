l=(5,56,3,2,76)
li=tuple(filter(lambda x:(x%2==0),l))
print(li)

age=(34,23,3)
adult=tuple(filter(lambda age:age>18,age))
print(adult)
