def cuboid(l,b,h):
    A=2*(l*b+h*b+h*l)
    return(A)

l=int(input("enter l"))
b=int(input("enter b"))
h=int(input("enter h"))
z=cuboid(l,b,h)
print(z)
