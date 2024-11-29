import os
def append():
    a=str(input("Enter file name="))
    if os.path.exists(a):
        f=open("gow.txt","a")
        f.write("september 30")
        f.close()
        
    else:
        a=str(input("Enter new file name="))
        f=open(a,"w")
        h=str(input("Do you want Enter content: yes/no"))
        if(h=='yes'):
            b=str(input("Enter content"))
            f.write(b)
            f.close()
            f=open(a,"r")
            print("Successfully added : " ,f.read())
        else:
            print("Thank you")
        
append()
