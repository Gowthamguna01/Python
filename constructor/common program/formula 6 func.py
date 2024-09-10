class Formula:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        
    def pcuboid(self):
        self.P=4*(self.l+self.b+self.h)
        print(self.P)


l=int(input("enter l"))
b=int(input("enter b"))
h=int(input("enter h"))


x=Formula(l,b,h)       
x.pcuboid()
