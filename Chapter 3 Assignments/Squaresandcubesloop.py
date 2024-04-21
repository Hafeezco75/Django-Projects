print('number\tsquare\tcube')
square = 2
cube = 3

for number in range(6):
	square = number ** 2
	cube = number ** 3
	print(f'{number}\t{square}\t{cube}')