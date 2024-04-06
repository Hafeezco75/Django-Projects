numbers = [13, 5, 7, 12, 9]

print('\n:')
print(f'Index  {"Value":>6}     Bar')

for index, value in enumerate(numbers):
	print(f'{index:>5}{value:>6}     {"*" * value}')