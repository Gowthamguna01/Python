class Forloop:
    def __init__(self,n):
        self.n=n
        
    def reverse(self):
        
        self.c=0
        for i in range(0,self.n+1):
            self.b=self.n%10 #rem(reverse pana)
            self.n=self.n//10 #quacent loop stop pana
            self.c=self.c*10+self.b #reverse changing
            print("reverse number=",self.c)
            if(self.n==0):
                break

n=int(input("enter n number="))
x=Forloop(n)
x.reverse()
