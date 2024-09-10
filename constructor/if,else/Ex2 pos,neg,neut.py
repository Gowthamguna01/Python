class Formula:
    def __init__(self,a):
        self.a=a
        
    def positive_negative(self):
        if(self.a>0):
            print("positive")
        elif(self.a<0):
            print("negative")
        elif(self.a==0):
            print("netural")


a=int(input("Enter a"))

x=Formula(a)            
x.positive_negative()
