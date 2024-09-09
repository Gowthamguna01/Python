dict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964",
    }

print(dict1)

#specific position
print(dict1["brand"])

#length
print(len(dict1))

#find type?
dict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964",
    "colors":["red","blue","white"]
    }

print(type(dict1))

#get function
x=dict1.get("model")
print(x)


#keys (key name)
x=dict1.keys()
print(x)

#values (key answer)
x=dict1.values()
print(x)

#items (show all key name//key values)
x=dict1.items()
print(x)

#if
if "model" in dict1:
    print("Yes, model is one of the keys in the dict")
    

#update
dict1.update({"year":2020})
print(dict1)

dict1.update({"color":"red"})
print(dict1)

print("=========================")


#new va oru row add panna
dict1["color"]="red"
print(dict1)


#pop
dict1.pop("model")
print(dict1)


print("==============================")

'''#pop item
dict1.popitem()
print(dict1)'''

#dict1.clear()
#print(dict1)

'''#delete panirum
del dict1["brand"]
print(dict1)'''




print("==============================")

#for loop
for x in dict1:
    print(x)

print("==============================")

for x in dict1:
    print(dict1[x])


print("==============================")

#for show values
for x in dict1.values():
    print(x)


print("==============================")

#for show keys
for x in dict1.keys():
    print(x)

print("==============================")


#x=brand y=values
for x,y in dict1.items():
    print(x,y)
    
print("==============================")


#copy
dict1=dict1.copy()
print(dict1)


print("==============================")
#changing dictory
mydict=dict(dict1)
print(mydict)






