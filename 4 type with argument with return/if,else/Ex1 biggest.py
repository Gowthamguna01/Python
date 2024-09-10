class Formula:
    def biggest(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
        if(self.a>self.b and self.a>self.c):
            return("A is big")
        elif(self.b>self.a and self.b>self.c):
            return("B is big")
        elif(self.c>self.a and self.c>self.b):
            return("c is big")


a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))

x=Formula()
v=x.biggest(a,b,c)
print(v)       
