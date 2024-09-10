class Formula:
    def negative_postive(self,a):
        self.a=a
        if(self.a>0):
            return("positive number")
        if(self.a<0):
            return("negative number")

a=int(input("Enter a="))

x=Formula()
v=x.negative_postive(a)
print(v)
