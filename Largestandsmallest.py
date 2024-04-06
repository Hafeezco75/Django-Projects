number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
number3 = int(input("Enter the third integer: "))
number4 = int(input("Enter the third integer: "))

smallest = number1

if number2 < smallest:
	smallest = number2

if number3 < smallest:
	smallest = number3

if number4 < smallest:
	smallest = number4

largest = number1

if number2 > largest:
	largest = number2

if number3 > largest:
	largest = number3

if number4 > largest:
	largest = number4

print('smallest is', smallest)
print('largest is', largest)

