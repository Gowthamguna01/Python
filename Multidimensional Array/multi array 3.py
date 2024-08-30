r=int(input("Enter row value="))
c=int(input("Enter col value="))
o=[] #outer box
for i in range(0,r):#n[i]
    m=[]
    for j in range(0,c):#n[j]
        b=int(input("values="))
        m.append(b)
    o.append(m)   
print(o)

l=[]
for i in range(0,r):
    h=[]
    for j in range(0,c):
        h.append(o[j][i])
        print(o[j][i],end=" ")
    l.append(h)
    print()
print(l)
