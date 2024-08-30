a=int(input("enter  a number="))
for i in range(1,a+1,1):
    for j in range(1,i+1,1):
        print(j,end="")
    print()
b=a-1
for c in range(1,b+1,1):
    d=c
    for d in range(1,b+1,1):
        print(d,end="")
    b=b-1
    print()

    
