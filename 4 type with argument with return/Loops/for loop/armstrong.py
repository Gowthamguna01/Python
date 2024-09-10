import math
class Formula:
    def armstrong(self,n):
        self.n=n
        self.c=len(str(self.n))
        self.a=self.n
        self.d=0
        for self.i in range(self.a,0,-1):
            self.b=self.a%10
            self.d=pow(self.b,self.c)+self.d
            self.a=self.a//10 #loop stop
    
        if(self.d==self.n):
            return("armstrong",self.d)
        else:
            return("not armstrong",self.d)
    
n=int(input("enter n num="))

x=Formula()
v=x.armstrong(n)
print(v)
