a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

x=max(n)
y=min(n)
print("max= ",x, "min= ",y)

m=[]
g=0
for i  in  range(a):
    if(x==n[i] or y==n[i]):
        print(" ")
    else:
        print("other values=",n[i])
        g=g+n[i]
        print("Total=",g)

F=a-2
final=g/F
print("value is= ", final)
    
        
    
