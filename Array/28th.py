a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

for i in range(a):
    if(n[i]==0 or n[i]==-1):
        print("")
    else:
        print("other values=",n[i])
