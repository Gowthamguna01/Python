small=lambda a,b,c,d:print("a is small")if(a<b and a<c and a<d)else print("b is small")if(b<c and b<d)else print("c is small")if(c<d)else print("d is small")

a=int(input("A value="))
b=int(input("b value="))
c=int(input("c value="))
d=int(input("d value="))
small(a,b,c,d)
