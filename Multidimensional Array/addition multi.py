r=int(input("Enter row="))
c=int(input("Enter col="))
o=[]
for i in range(0,r): #i
    IN=[]
    for j in range(0,c):#j
        b=int(input("values="))
        IN.append(b)
    o.append(IN)#1 array
print(o)

ou=[]
for i in range(0,r):#i
    IN=[] #IN box name
    for j in range(0,c):#j
        b=int(input("values="))
        IN.append(b)
    ou.append(IN)#2 array
print(ou)

m=[]
for i in range(0,r):
    for j in range(0,c):
        a=o[i][j]+ou[i][j]#addition
        m.append(a)
    print(m)
    
    


        
