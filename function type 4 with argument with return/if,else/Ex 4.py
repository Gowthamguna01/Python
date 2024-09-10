def grade(TAM,ENG,MAT,SCI,SOC):
    
    b=TAM+ENG+MAT+SCI+SOC
    c=b/5
    if(c>85 and c<=100):
        return("A grade")
    elif(c>70 and c<=85):
        return("B grade")
    elif(c>50 and c<=70):
        return("C grade")
    elif(c>35 and c<=50):
        return("D grade")
    elif(c<35):
        return("Fail")


TAM=int(input("Enter TAM:"))
ENG=int(input("Enter ENG:"))
MAT=int(input("Enter MAT:"))
SCI=int(input("Enter SCI:"))
SOC=int(input("Enter SOC:"))
z=grade(TAM,ENG,MAT,SCI,SOC)
print(z)


