class Formula:
    def second_number(self,a,b):
        self.a=a
        self.n=[]
        for self.i in range(0,self.a):
            self.b=int(input("values="))
            self.n.append(self.b)
        self.n[1]=50
        return(self.n)

a=int(input("enter a number="))

x=Formula()
v=x.second_number(a,b)
print(v)
