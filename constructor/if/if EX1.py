class Formula:
    def __init__(self,n):
        self.n=n
        
    def oddeven(self):
        
        if(self.n%2==0):
            print("Even number")
        if(self.n%2==1):
            print("Odd number")


n=int(input("enter n="))
x=Formula(n)
x.oddeven()
