r=int(input("enter row="))
c=int(input("enter col="))
o=[]
for i in range(0,r):
    m=[]
    for j in range(0,c):
        b=int(input("Value="))
        m.append(b)
    o.append(m)
print(o)

l=[] #outer box
for i in range(0,r):#row
    h=[] #inner box
    for j in range(0,c):#col
        h.append(o[j][i])
        print(o[j][i],end=" ")
    l.append(h)
    print()
print(l)

if(o[j][i]==l[j][i]):
    print("symmtric matrix")

else:
    print("Not symmentric")
