class pattern:
    def trianglestar(self):
        self.a=int(input("enter a number="))
        self.g=1
        for g in range(1,self.a,1):
            
            self.k=self.a-self.g
            for k in range(self.k,0,-1):
                print(" ",end="")
                
            self.j=1
            for j in range(1,self.g,1):
                print("*",end="")
            print("*",end="")
            
            self.v=self.g-1
            for v in range(self.v,0,-1):
                print("*",end="")
            print()
            
        self.c=self.a-1
        for c in range(self.c+1,0,-1):
            self.k=self.a-self.c
            
            for k in range(self.k,0,-1):
                print(" ",end="")
                
            self.s=1
            for s in range(1,self.c+1,1):
                print("*",end="")
                
            self.d=self.c-1
            for d in range(self.d,0,-1):
                print("*",end="")
            print()

x=pattern()            
x.trianglestar()
    
        
        
    
    
    
