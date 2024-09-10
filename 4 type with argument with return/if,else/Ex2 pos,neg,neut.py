class Formula:
    def positive_negative(self,a):
        self.a=a
        if(self.a>0):
            return("positive")
        elif(self.a<0):
            return("negative")
        elif(self.a==0):
            return("netural")

a=int(input("Enter a"))

x=Formula()
v=x.positive_negative(a)
print(v)
