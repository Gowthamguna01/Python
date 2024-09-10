class Formula:
    def first_last(self,a,b):
        self.a=a
        self.n=[]
        for self.i in range(0,self.a):
            self.b=int(input("values="))
            self.n.append(self.b)
        return(self.n[0],self.n[4])

a=int(input("enter a number="))


x=Formula()
v=x.first_last(a,b)
print(v)
