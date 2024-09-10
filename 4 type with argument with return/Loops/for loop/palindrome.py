class Formula:
    def palindrome(self,a):
        self.a=a
        self.n=self.a
        self.b=0
        for self.i in range(0,self.a+1):
            if(self.a>0):
                self.c=self.a%10
                self.a=self.a//10
                self.b=self.b*10+self.c
                
        if(self.b==self.n):
            return("palindrome",self.b)
        else:
            return("not a palindrome",self.b)
        return(self.b)


a=int(input("enter a number="))
x=Formula() 
v=x.palindrome(a)
print(v)
