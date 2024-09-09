def star(a):
    
    for i in range(1,a+1,1):
        for j in range(1,11,1):
            print("*", end="")
        print()

a=int(input("enter a num"))
star(a)
            
