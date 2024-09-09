a=int(input("enter a num="))
g=1
while(g<=a):
    k=a-g
    while(k>=1):
        print(" ",end="")
        k=k-1
    j=1
    while(j<g):
        print(j,end="")
        j=j+1
    print(g,end="")
    v=g-1
    while(v>=1):
        print(v,end="")
        v=v-1
    g=g+1
    print()
c=a-1
