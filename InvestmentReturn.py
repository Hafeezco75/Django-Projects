principal = int(input("Enter the original amount invested "))

annualrate = 7 / 100

numberofyears = int(input("Enter the number of years "))

flat = 1 + annualrate

base = flat ** numberofyears

amountofdeposit = principal * base

print(amountofdeposit)