class Formula:
    def natural(self,n):
        self.n=n
        self.b=0
        for self.i in range(1,self.n+1,1):
            self.b=self.b+self.i
            self.i=self.i+1
        return(self.b)

n=int(input("Enter number"))

x=Formula()
v=x.natural(n)
print(v)        
