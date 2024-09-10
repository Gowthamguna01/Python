import math
class Formula:
    def armstrong(self,n):
        self.n=n
        self.c=0
        self.a=self.n
        self.d=0
        self.m=self.n
        
        while(self.n>0):
            self.n=self.n//10
            self.c=self.c+1
            
        while(self.a>0):
            self.b=self.a%10
            self.d=pow(self.b,self.c)+self.d
            self.a=self.a//10

        if(self.d==self.m):
            return("armstrong",self.d)
        else:
            return("not armstrong",self.d)

n=int(input("enter n num="))

x=Formula()
v=x.armstrong(n)
print(v)
