class Formula:
    def small(self,x,y):
        self.a=a
        self.b=b
        if(self.a<self.b):
            return("A is small")
        if(self.b<self.a):
            return("B is small")

a=int(input("Enter a="))
b=int(input("ENTER b="))

x=Formula()
v=x.small(a,b)
print(v)
