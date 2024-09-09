tuple1=(11,22)
tuple2=(99,88)

y=tuple2[0],tuple2[1]
tuple2=tuple1[0],tuple1[1]
tuple1=y[0],y[1]

print(tuple2)#11,22
print(tuple1)#99,88
