def multi(r,c):
    o=[]
    for i in range(0,r):
        n=[]
        for j in range(0,c):
            b=int(input("Enter values="))
            n.append(b)
        o.append(n)
    print(o)
    l=[]
    for i in range(0,r):
        h=[]
        for j in range(0,c):
            h.append(o[j][i])
            print(o[j][i],end=" ")
        l.append(h)
    print()
    for i in range(0,1):
        if(o[j][i]== 0 and 1 or 1 and 0):
            print("idetity matrix")
        else:
            print("not identity matrix")


r=int(input("Enter row="))
c=int(input("enter col="))
multi(r,c)
    
    
