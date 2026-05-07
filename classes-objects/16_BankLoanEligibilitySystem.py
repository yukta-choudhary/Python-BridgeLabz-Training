# Problem 17: Bank Loan Eligibility System
# Scenario: Check loan eligibility
# Task: Return True or False

class LoanApplicant:

    def __init__(self, name, salary, credit_score):
        self.name = name
        self.salary = salary
        self.credit_score = credit_score

    def is_eligible(self):

        if self.salary > 50000 and self.credit_score > 700:
            return True

        else:
            return False


# Creating object
applicant = LoanApplicant("Riya", 80000, 750)

# Printing eligibility
print(applicant.is_eligible())