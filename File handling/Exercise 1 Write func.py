import os
def write():
    a=str(input("Enter file name="))
    if os.path.exists(a):
        f=open(a,"w")
        f.write("Hyderabed,Gachibowli,Gowtham")
        f.close()
        print("File Successfully updated :) [visit notepad] ") #Refresh Everytime
        
    else:
        print("File not Available :( ")
        g=(input("Do you want Create a New file: yes/no"))

        
        if(g=="yes"):
            f=open(a,"w")
            h=str(input("Do you want Enter content: yes/no"))

            if(h=='yes'):
                b=str(input("Enter Content"))
                f.write(b)
                f.close()
            else:
                print("Thank you")
        
write()

#27sep
#File Handling
