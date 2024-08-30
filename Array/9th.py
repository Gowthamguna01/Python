a=int(input("enter a number="))
n=[]
x=[]
v=[]
for i in range(a):
    b=int(input("n values="))
    n.append(b)
print(n)
for i in range(a):
    c=int(input("x values="))
    x.append(c)
    g=n[i]+x[i]
    v.append(g)
print(v)
