class NotEligible(Exception):
    pass

def eligiblityForLoan():
    eligiblesalary=15000
    eligiblecibil=700
    try:
        salary=int(input("Enter your monthly salary:"))
        cibil=float(input("Enter cibil score:"))
        if(salary<eligiblesalary or cibil<eligiblecibil):
            raise NotEligible
        else:
            print("your records is eligible for sanctaning loan")
    except NotEligible:
        print("you doesn't have enough credit for applying loan")
        eligiblityForLoan()

eligiblityForLoan()
        
