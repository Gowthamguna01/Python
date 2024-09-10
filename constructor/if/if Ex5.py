class Formula:
    def __init__(self,a):
        self.a=a
                
    def negative_postive(self):
        if(self.a>0):
            print("positive number")
        if(self.a<0):
            print("negative number")


a=int(input("Enter a="))

x=Formula(a)            
x.negative_postive()
