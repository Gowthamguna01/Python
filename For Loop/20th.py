a=int(input("enter a number="))
i=1
for i in range(1,a+1):
    m=i
    for j in range(1,i+1,1):
        print(m,end="")
        m=m+a-j
    print()
        
