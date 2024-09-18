class InvalidAge(Exception):
    pass 

def calculate():
    number=18
    try:
        age=int(input("Enter age: "))
        if(age<number):
            raise InvalidAge
        else:
            print("age is eligible for vote")
    except InvalidAge:
        print("age is not eligibe for voting")
        calculate()
calculate()
