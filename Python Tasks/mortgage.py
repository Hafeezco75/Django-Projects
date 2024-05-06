PrincipalAmount = int(input("Enter the principal amount: "))

Annualrate = int(input("Enter the annual interest rate: "))

numberofYears = int(input("Enter the duration in years: "))

NoOfYears = 12 * numberofYears

rate = Annualrate / 100

MonthlyRate = rate / 12

monthbase = 1 + MonthlyRate

base = monthbase ** NoOfYears

num1 = PrincipalAmount * MonthlyRate

num2 = base - 1

Monthlypayment = num1 * base / num2


print(Monthlypayment)

