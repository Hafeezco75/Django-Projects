score = int(input("Enter a score: "))
Grade = 100

if score >= 80 and score <= Grade:
	print('Your grade is A, you passed')
elif score >= 65 and score <= 79 :
	print('Your grade is B, you passed')
elif score >= 50 and score <= 64 :
	print('Your grade is C')
elif score >= 40 and score <= 49 :
	print('Your grade is D')
elif score >= 0 and score <= 39 :
	print('You Failed')



