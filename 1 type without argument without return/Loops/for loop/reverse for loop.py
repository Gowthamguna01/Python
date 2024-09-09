def reverse():
    n=int(input("enter n number="))
    c=0
    for i in range(0,n+1):
        b=n%10 #rem(reverse pana)
        n=n//10 #quacent loop stop pana
        c=c*10+b #reverse changing
        print("reverse number=",c)
        if(n==0):
            break
reverse()
