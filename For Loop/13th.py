a=int(input("enter a num="))
c=a
for i in range(1,a+1,1):#down
    for j  in range(1,a+1,1):#rightside
        print(j,end="")
    a=a-1
    print()
