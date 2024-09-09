list1=["Hello", "take"]
list2=["Dear", "Sir"]

b=len(list1)
for i in range(0,b,1):
    list3=[]
    for j in range(0,b,1):
        c=list1[i]+list2[j]
        list3.append(c)
    print(list3)
