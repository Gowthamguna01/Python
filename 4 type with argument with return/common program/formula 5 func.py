class Formula:
    def cuboid(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        self.A=2*(self.l*self.b+self.h*self.b+self.h*self.l)
        return(self.A)

l=int(input("enter l"))
b=int(input("enter b"))
h=int(input("enter h"))

x=Formula()
v=x.cuboid(l,b,h)
print(v)
