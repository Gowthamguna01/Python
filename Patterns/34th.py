n=int(input("enter a num="))
i=n
v=n
while(i>=1):
    sp=i-1
    while(sp>=1):#space
        print(sp,end="")
        sp=sp-1
    g=1
    while(g<=n):
        h=1
        while(h<=g):
            print(h,end="")
            h=h+1
        g=g+1
    i=i-1
    print()
