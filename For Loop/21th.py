a=int(input("enter a number="))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")#only space
        
    for j in range(2*i+2):
        if(j==0):
            print(" ",end="")
        else:
            print(j,end="")
    print()
