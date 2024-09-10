class Formula:
    def natural(self,n):
        self.n=n
        self.i=1
        self.b=0
        while(self.i<=self.n):
            self.b=self.b+self.i
            self.i=self.i+1
        return(self.b)

n=int(input("Enter number"))

x=Formula()
v=x.natural(n)
print(v)        
