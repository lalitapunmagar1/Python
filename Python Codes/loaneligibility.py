def check_loan_eligibility(age, stable_income, credit_score, criminal_record, loan_default):
    if 18<=age <= 65 and stable_income=="yes":
        return "Eligible for loan based on age and stable income."
    if credit_score>700:
        return "Eligible for loan based on credit score."
    if criminal_record=="yes":
        return "Not eligible for loan due to criminal record."
    if loan_default=="yes":
        return "Not eligible for loan due to previous loan default."
    return "Not eligible for a loan based on the given criteria."
def main():
    age= int (input("Enter your age:"))
    stable_income=input("Do you have a stable income? (yes/no):")
    credit_score=int (input("Enter your credit score:"))
    criminal_record=input("Do you have criminal record?(yes/no):")
    loan_default=input("Have you defaulted on a loan before? (yes/no):")
    
    eligibility= check_loan_eligibility(age, stable_income, credit_score, criminal_record, loan_default)
    print(eligibility)
main()