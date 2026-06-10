age = int(input("Enter Age: "))
salary = int(input("Enter Salary: "))

if age >= 18:
    if salary >= 25000:
        print("Eligible for Loan")
    else:
        print("Salary Criteria Not Met")
else:
    print("Age Criteria Not Met")
