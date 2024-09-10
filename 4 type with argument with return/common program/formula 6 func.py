class  Formula:
    def pcuboid(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        self.P=4*(self.l+self.b+self.h)
        return(self.P)


l=int(input("enter l"))
b=int(input("enter b"))
h=int(input("enter h"))

x=Formula()        
v=x.pcuboid(l,b,h)
print(v)
