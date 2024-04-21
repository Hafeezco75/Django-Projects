counter = 1

n = int(input("Enter a non-negative integer "))

factorial = (n - 1) * (n - 2) * 1 

for numbers in range(n):

	counter -= counter

	numbers *= factorial

	print(f'{numbers}')

