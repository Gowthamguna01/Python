r=int(input("Enter row="))
c=int(input("Enter col="))
o=[]
ou=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        b=int(input("b value="))
        n.append(b)
    o.append(n)
print(o)

ou=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        b=int(input("b value="))
        n.append(b)
    ou.append(n)
print(ou)


g=[[0,0],[0,0]]
for i in range(0,r):
    for j in range(len(ou[0])):
        for k in range(len(ou)):
            g[i][j]+=o[i][k]*ou[k][j]
for c in g:
    print(c)



