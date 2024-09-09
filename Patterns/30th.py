a=int(input("enter a num="))
g=1
while(g<=a):
    k=a-g
    while(k>=1):
        print(" ",end="")
        k=k-1
    j=1
    while(j<g):
        print("*",end="")
        j=j+1
    print("*",end="")
    v=g-1
    while(v>=1):
        print("*",end="")
        v=v-1
    g=g+1
    print()
c=a-1
while(c>=1):
    k=a-c
    while(k>=1):
        print(" ",end="")
        k=k-1
    s=1
    while(s<=c):
        print("*",end="")
        s=s+1
    d=c-1
    while(d>=1):
        print("*",end="")
        d=d-1
    c=c-1
    print()
