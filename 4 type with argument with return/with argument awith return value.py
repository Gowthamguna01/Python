class Formula:
    def addition(self,a,b):
        self.a=a
        self.b=b
        self.c=a+b
        return(self.c)


a=int(input("enter a"))
b=int(input("enter b"))

x=Formula()
v=x.addition(a,b)
print(v)
