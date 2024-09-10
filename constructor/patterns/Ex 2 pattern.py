class pattern:
    def star(self):
        self.a=int(input("enter a number="))
        n=self.a+3
        c=self.a
        
        for c in range(self.a,0,-1):
            k=self.a-c
            
            for k in range(k,0,-1):
                print(" ",end="")

            s=1
            for s in range(1,c,1):
                print("*",end="")
        
            d=c-1
            for d in range(d+1,0,-1):
                print("*",end="")
            print()
        
        g=1
        for g in range(1,self.a+1,1):
            k=self.a-g

            for k  in range(k+1,0,-1):
                print(" ",end="")
                
            j=1
            for j in range(1,g-1,1):
                print("*",end="")
                
            v=g-1
            for v in range(v,0,-1):
                print("*",end="")
            g=g+1
            print()
        
            q=1
            y=self.a+4
        for q in range(1,y+1,1):
            print("*",end="")

x=pattern()
x.star()
    
            
