a=int(input("enter a number="))
n=[]
for i in range(0,a):
    b=int(input("enter a value="))
    n.append(b)
print(n)
c=int(input("enter a value="))
x=[]

for i in range(a):
    if(c != n[i] ):
        x.append(n[i])

print(x)


