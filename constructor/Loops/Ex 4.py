class Loops:
    def __init__(self,n):
        self.n=n
        
    def currentandprevious(self):
        while(self.n>0):
            if(self.n%2==1):
                self.b=self.n-2
                print("current num=",self.n)
                if(self.b>0):
                    print("previous num=",self.b)
                    self.n=self.n-1

n=int(input("enter n number="))
x=Loops(n)
x.currentandprevious()
