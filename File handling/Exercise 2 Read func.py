import os
def read():
    a=str(input("Enter file name="))
    if os.path.exists(a):
        f=open(a,"r")
        print(f.read())

    else:
        a=str(input("Enter new file name="))
        f=open(a,"w")
        h=str(input("Do you want Enter content: yes/no"))
        if(h=='yes'):
            b=str(input("Enter content"))
            f.write(b)
            f.close()
        else:
            print("Thank you")
        
read()
