a=int(input("enter a num="))
g=1
while(g<=a):
    k=a-g
    while(k>=1):
        print(" ",end="")
        k=k-1
    j=1
    while(j<g):
        if(j==1):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    if(g==1):
        print("*",end="")
    else:
        print(" ",end="")
    v=g-1
    while(v>=1):
        if(v==1):
            print("*",end="")
        else:
            print(" ",end="")
        v=v-1
    g=g+1
    print()
q=1
y=a+4
while(q<=y):
    print("*",end="")
    q=q+1
    
