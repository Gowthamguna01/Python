class Forloops:
    def __init__(self,a):
        self.a=a
    
    def palindrome(self):
        
        self.n=self.a
        self.b=0
        for i in range(0,self.a+1):
            self.c=self.a%10
            self.a=self.a//10
            self.b=self.b*10+self.c
            print(self.b)
            if(self.a==0):
                break
        if(self.b==self.n):
            print("palindrome",self.b)
        else:
            print("not a palindrome",self.b)

a=int(input("enter a number="))
x=Forloops(a)            
x.palindrome()
