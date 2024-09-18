class Password(Exception):
    pass

def check():
    mobile=1234
    i=0
    try:
        while(i<3):
            num=int(input("enter password="))
            if(mobile==num):
                raise Password
            else:
                print("phone is locked")
            i=i+1
            
    except Password:
        print("password correct")
        return
        check()
                
check()

