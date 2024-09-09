tuple1=(('a',23),('b',37),('c',11),('d',29))
y=list(tuple1)
b=sorted(y, key=lambda x:x[1])
print(b)
