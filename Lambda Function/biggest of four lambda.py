big=lambda a,b,c,d:print("a is bigger")if(a>b and a>c and a>d)else print("b is bigger")if(b>c and b>d)else print("c is bigger")if(c>d)else print("d is bigger")

a=int(input("Enter a value="))
b=int(input("Enter b value="))
c=int(input("Enter c value="))
d=int(input("Enter d value="))
big(a,b,c,d)
