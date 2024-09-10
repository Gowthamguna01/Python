class Formula:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def biggest(self):
        if(self.a>self.b and self.a>self.c):
            print("A is big")
        elif(self.b>self.a and self.b>self.c):
            print("B is big")
        elif(self.c>self.a and self.c>self.b):
            print("c is big")


a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))

x=Formula(a,b,c)
x.biggest()
        
