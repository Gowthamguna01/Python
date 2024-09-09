def currentandprevious(n):
    
    while(n>0):
        if(n%2==1):
            b=n-2
            print("current num=",n)
            if(b>0):
                print("previous num=",b)
        n=n-1


n=int(input("enter n number="))
currentandprevious(n)
