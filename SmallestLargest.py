number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
number3 = int(input("Enter the third integer: "))

sum = number1 + number2 + number3

average = (number1 + number2 + number3) / 3

product = number1 * number2 * number3

smallest = number1

if number2 < smallest:
	smallest = number2

if number3 < smallest:
	smallest = number3

largest = number1

if number2 > largest:
	largest = number2

if number3 > largest:
	largest = number3

print('sum is', sum)
print('average is', average)
print('The product is', product)
print('smallest is', smallest)
print('largest is', largest)
