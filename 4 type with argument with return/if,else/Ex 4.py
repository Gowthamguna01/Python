class Formula:
    def grade(self,TAM,ENG,MAT,SCI,SOC):
        self.b=TAM+ENG+MAT+SCI+SOC
        self.c=self.b/5
        if(self.c>85 and self.c<=100):
            return("A grade")
        elif(self.c>70 and self.c<=85):
            return("B grade")
        elif(self.c>50 and self.c<=70):
            return("C grade")
        elif(self.c>35 and self.c<=50):
            return("D grade")
        elif(self.c<35):
            return("Fail")


TAM=int(input("Enter TAM:"))
ENG=int(input("Enter ENG:"))
MAT=int(input("Enter MAT:"))
SCI=int(input("Enter SCI:"))
SOC=int(input("Enter SOC:"))

x=Formula()
v=x.grade(TAM,ENG,MAT,SCI,SOC)
print(v)


