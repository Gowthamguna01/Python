class Formula:
    def oddeven(self,n):
        self.n=n
        if(self.n%2==0):
            return("Even number")
        if(self.n%2==1):
            return("Odd number")


n=int(input("enter n="))

x=Formula()
v=x.oddeven(n)
print(v)
