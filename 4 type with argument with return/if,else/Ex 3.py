class Formula:
    def arithmatic(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
        if(self.c=="1" or self.c=="+"):
            self.d=self.a+self.b
            return(self.d)
        
        elif(self.c=="2" or self.c=="-"):
            self.d=self.a-self.b
            return(self.d)
        
        elif(self.c=="3" or self.c=="*"):
            self.d=self.a*self.b
            return(self.d)
        
        elif(self.c=="4" or self.c=="/"):
            self.d=self.a/self.b
            return(self.d)
        
        elif(self.c=="5" or self.c=="%"):
            self.d=self.a%self.b
            return(self.d)

a=int(input("enter a"))
b=int(input("enter b"))
c=str(input("enter sign"))

x=Formula()
v=x.arithmatic(a,b,c)
print(v)
