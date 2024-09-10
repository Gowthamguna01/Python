class Formula:
    def biggest(self,a,b):
        self.a=a
        self.b=b
        if(self.a>self.b):
            return("A is BIG")
        if(self.b>self.a):
            return("B is BIG")

a=int(input("Enter a="))
b=int(input("ENTER b="))

x=Formula()
v=x.biggest(a,b)
print(v)
