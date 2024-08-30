r=int(input("Enter row value="))
c=int(input("Enter col value="))
o=[] #outer box
tem=0
for i in range(0,r):
    In=[] #inner box
    for j in range(0,c):
        b=int(input("value="))
    o.append(In)
print(o)



for i in range(0,c):
    for j in range(0,r):
        print(o[j][i],end=" ")
    print()
