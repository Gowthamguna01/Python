class Formula:
    def palindrome(self,a):
        self.a=a
        self.d=0
        self.c=self.a
        while(self.a>0):
            self.b=self.a%10
            self.a=self.a//10
            self.d=self.d*10+self.b
        
        if(self.d==self.c):
            return("palindrome",self.d)
        else:
            return("not a palindrome",self.d)

        return(self.d)

  
a=int(input("enter a number="))

x=Formula()
v=x.palindrome(a)
print(v)
