def cuboid():
    l=int(input("enter l"))
    b=int(input("enter b"))
    h=int(input("enter h"))
    A=2*(l*b+h*b+h*l)
    return(A)
    
x=cuboid()
print(x)
