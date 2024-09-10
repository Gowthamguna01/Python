class  Formula:
    def reverse(self,n):
        self.n=n
        self.c=0
        for self.i in range(0,self.n,1):
            if(self.n>0):
                self.b=self.n%10 #rem(reverse pana)
                self.n=self.n//10 #quacent loop stop pana
                self.c=self.c*10+self.b #reverse changing
        return("reverse number=",self.c)

n=int(input("enter n number="))

x=Formula()
v=x.reverse(n)
print(v)
