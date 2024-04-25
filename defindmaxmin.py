def find_maximum(numbers):

	numbers = [8, 4, 9, 2, 5, 7, 3]

	for maximum in numbers:

		if numbers > maximum:

			maximum = numbers

	return maximum(numbers)


def find_minimum(numb):

	numb = [8, 4, 9, 2, 5, 7, 3]

	for minimum in numb:

		if minimum < numb:

			minimum = numb

	return minimum(numb)
