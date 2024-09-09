def reverse(n):
    
    c=0
    for i in range(0,n,1):
        if(n>0):
            b=n%10 #rem(reverse pana)
            n=n//10 #quacent loop stop pana
            c=c*10+b #reverse changing
    return("reverse number=",c)

n=int(input("enter n number="))
x=reverse(n)
print(x)
