def grade():
    TAM=int(input("Enter TAM:"))
    ENG=int(input("Enter ENG:"))
    MAT=int(input("Enter MAT:"))
    SCI=int(input("Enter SCI:"))
    SOC=int(input("Enter SOC:"))
    b=TAM+ENG+MAT+SCI+SOC
    c=b/5
    if(c>85 and c<=100):
        print("A grade")
    elif(c>70 and c<=85):
        print("B grade")
    elif(c>50 and c<=70):
        print("C grade")
    elif(c>35 and c<=50):
        print("D grade")
    elif(c<35):
        print("Fail")
grade()


