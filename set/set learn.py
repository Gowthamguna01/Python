thisset={"apple","banana","orange"}
print(thisset)

#for loop
for x in thisset:
    print(x)

#present check
thisset={"apple","banana","orange"}
print("banana" in thisset)

#add
thisset.add("lion")
print(thisset)


#update
thisset.update(["mango","graphs","papaya"])
print(thisset)


#remove
thisset.remove("banana")
print(thisset)


#discard
thisset.discard("lion")
print(thisset)

#pop => any element remove
x=thisset.pop()
print(x) #entha element remove aguchi.
print(thisset)#balance iruka element SHOW AGUM


print("-------------------------------------")

#clear
thisset={"apple","banana","cherry"}
thisset.clear() 
print(thisset)

#del
thisset={"apple","banana","cherry"}



#union
set1={1,2,3}
set2={"a","b","c"}
set3=set1.union(set2)
print(set3)

#update
set1={1,2,3}
set2={"hi","a","b","c"}
set1.update(set2)
print(set1)

#intersection
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.intersection(y)
print(z)

#compare 3 set
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}

result=x.intersection(y,z)
print(result)


#Difference
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.difference(y)
print(z)

#disjoint
x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.isdisjoint(y)
print(z)


#issubset
x={"a","b","c"}
y={"f","e","d","c","b","a"}
z=x.issubset(y)
print(z)

print("================================")

#issuperset
x={"a","b","c","m","d"}
y={"f","e","d","u","m"}
z=x.issuperset(y)
print(z)

#issymmetric difference
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)






















