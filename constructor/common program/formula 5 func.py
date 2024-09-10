class Formula:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        
    def cuboid(self):
        self.A=2*(self.l*self.b+self.h*self.b+self.h*self.l)
        print(self.A)



l=int(input("enter l"))
b=int(input("enter b"))
h=int(input("enter h"))

x=Formula(l,b,h)
x.cuboid()
