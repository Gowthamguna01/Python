class  Formula:
    def perimeter_of_triangle(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.P=self.a+self.b+self.c/2
        return(self.P)


a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))

x=Formula()
v=x.perimeter_of_triangle(a,b,c)
print(v)
