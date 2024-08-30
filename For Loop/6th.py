a=int(input("enter a num="))
c=a
for i in range(1,a,1):#down
    for j  in range(1,a+1,1):#rightside
        print(j,end="")
    a=a-1
    print()
for i in range(1,c+1,1):
    for j in range(1,i+1,1):
        print(j,end="")
    c=c-1
    print()

