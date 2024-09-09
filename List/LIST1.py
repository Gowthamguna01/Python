List1=["yuva","sakthi","academy"]
print(List1)


list2=[1,5,7,9,3]  #numbers
print(list2)

list3=[True,False,False]
print(list3)

list4=["abc",34,True,40,"male"] #mix
print(list4)

print(type(list2))  #list //what type?

list5=list(("apple","mango","orange","banana","graphs","pineapple")) #list kulla list
print(list5)
'''---------------------------------------------------'''
#positions

print(list5[1]) #positions

print(list5[-1]) #[-1] last position kattum

print(list5[2:5]) #2nd position to 5th position kula iruka values kattum

print(list5[:3]) #apple,mango,orange 1st three showing

print(list5[1:]) #1st position mattum vitutu mathathu elam print panum

'''-----------------------------------------------------------'''
print(list5[-4:-1]) #positions vachi show panum. (4th to 1st positions varaikum)


if("yuva" in List1): #checking
    print("yes,yuva in the list")

List1[1]="systems"
print(List1[1])      #replaceing
print(List1)

List1[1:3]=["kalpana","sakthi"]
print(List1)

List1[1:2]=["kalpana","sakthi"] #1 laa change agum
print(List1[1:2])

List1[1:3]=["SAKTHI"] #1,-----,3 ithu change pana
print(List1)

#INSERT
List1.insert(2,"john wick")
print(List1)

#APPEND
List1.append("good")
print(List1)

#EXTAND
list2.extend(list3)
print(list2)

#REMOVE
List1.remove("good")
print(List1)

#POP
List1.pop(0)
print("hi ",List1)

List1.pop()
print(List1)

#DELETE
del List1[0]
print(List1)

#clear
List1.clear()
print(List1)

#FOR
for x in List1: #ONU ONaa print agum for loop la
    print(x)

List1=["gowtham","mani","good","guna"]
print(List1)


#len
for i in range(len(List1)):
    print(List1[i])

#while loop
i=0
while(i<len(List1)):
    print(List1[i])
    i=i+1

[print(x) for x in List1] #one line


 
#array store to another array
'''fruits=["apple","banana","orange","a"]
newlist=[]
for x in fruits:
    if "a" in x:
    newlist.append(x)
    print(newlist)'''

list2=["LION","TIGER","ELephant","MONkey"]

#....
list2.sort()
print(list2)

#reversed
list2.sort(reverse=True)
print(list2)

#LOWER
list2.sort(key=str.lower)
print("LOWER= ",list2)

#copy pani inoru  array la store
list7=list2.copy()
print(list7)

#ADDITION
list3=List1+list2
print(list3)







