def previousnum():
    n=int(input("enter n number="))
    while(n>0):
        if(n%2==0):
            print("current number=",n)
            b=n-2
            print("previous number=",b)
        n=n-1
previousnum()
