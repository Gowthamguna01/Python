a=str(input("enter a value="))
b=len(a)-1
g=0
while(g<=b):
    k=b-g
    while(k>=0):
        print(" ",end="")
        k=k-1
    j=0
    while(j<g):#start
        if(j==0):
            print(a[g],end="")
        else:
            print("@",end="")
        j=j+1
        
    if(g==0):#center
        print(a[g],end="")
    else:
        print("#",end="")
    v=g-1
    while(v>=0):#end
        if(v==0):
            print(a[g],end="")
        else:
            print("*",end="")
        v=v-1
    g=g+1
    print()
g=0
while(g<=b):
    k=b-g
    while(k>=0):
        print(" ",end="")
        k=k-1
    g=g+1
h=b-1
m=0
while(h>=m):
    print(a[h],end="")
    h=h-1
    while(u<=):
    print()
    

