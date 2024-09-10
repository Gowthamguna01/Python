def palindrome():
    a=int(input("enter a number="))
    n=a
    b=0
    for i in range(0,a+1):
        if(a>0):
            c=a%10
            a=a//10
            b=b*10+c
            
    if(b==n):
        return("palindrome",b)
    else:
        return("not a palindrome",b)

    return(b)
x=palindrome()
print(x)
