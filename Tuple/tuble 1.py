tuple1=("apple","banana","cherry")
print(tuple1)

tuple1=("apple","banana","cherry","apple","cherry")
print(tuple1)
print(len(tuple1))

tuple1=("apple")
print(type(tuple1))


tuple1=(1,2,3,4,5)
print(tuple1)

tuple1=(True,False,False)
print(tuple1)


tuple1=tuple(("apple","orange","banana","mango"))
print(tuple1)
print(tuple1[-1])
print(tuple1[2:5])
print("--------------------")
print(tuple1[:3])
print(tuple1[1:])
print(tuple1[-4:-1])

print("===================================")

tuple2=["benz","audi","bmw"]
tuple2.append("vowls wagen")
print(tuple2)

#converting tuple to list again list to tuple  
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("lion")
thistuple=tuple(y)
print(y)

print("--------------------------------------")

fruits=("apple","banana","cherry","lion")
(green,yellow,red,brown)=fruits
print(green)
print(yellow)
print(red)
print(brown)




