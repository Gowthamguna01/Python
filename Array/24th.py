a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

m=[]
for j in range(a):
    c=int(input("enter values="))
    m.append(c)
print(m)

for i in range(a):
    if(n[i]==m[i]):
        print("Equal=",n[i],m[i])

    else:
        print("Not Equal",n[i],m[i])
    
