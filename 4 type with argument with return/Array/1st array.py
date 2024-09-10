class Formula:
    def thirdlast(self,a,v):
        self.a=a
        self.n=[]
        for i in range(self.a):
            self.v=v
            self.n.append(self.v)
            return(self.n[2],self.n[3])

a=int(input("enter a value="))
v=int(input("value:"))

x=Formula()
v=x.thirdlast(a,v)
print(v)

