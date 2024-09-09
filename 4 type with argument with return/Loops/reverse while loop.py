def reverse(a):
    
    c=0
    while(a>0):
        b=a%10 #rem(reverse pana)
        a=a//10 #quacent loop stop pana
        c=c*10+b #reverse changing
    return("reverse number=",c)


a=int(input("enter n number="))
x=reverse(a)
print(x)

