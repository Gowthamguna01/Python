def palindrome(a):
    
    n=a
    b=0
    for i in range(0,a+1):
        c=a%10
        a=a//10
        b=b*10+c
        print(b)
        if(a==0):
            break
    if(b==n):
        print("palindrome",b)
    else:
        print("not a palindrome",b)


a=int(input("enter a number="))
palindrome(a)
