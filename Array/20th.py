#get input
a=int(input("enter a number="))
s=[]
for i in range(a):
    b=str(input("enter values="))
    s.append(b)
print(s)

#duplicate
dup=[]
for i in range(a):
    for j in range(i+1,a):
        if(s[i]==s[j] and s[i] not in dup):
            dup.append(s[i])
#check
if(dup):
    print("duplicates strings=",dup)
else:
    print("no duplicates")
