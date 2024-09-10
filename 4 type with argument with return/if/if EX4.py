class Formula:
    def eligible(self,a):
        self.a=a
        if(self.a>=18):
            return("Eligible for vote")
        if(self.a<18):
            return("Not Eligible for vote")

a=int(input("enter a num="))

x=Formula()
v=x.eligible(a)
print(v)
