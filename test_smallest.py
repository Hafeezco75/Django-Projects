from smallest import pass_list

def test_for_numbers_returns_smallest():
	assert pass_list(2, 5, 9) == 2
	assert pass_list(3, 6, 8) == 3

def test_for_numbers_returns_numb_or_numbs_or_number():
	assert pass_list(4, 0, 7) == 4
	assert pass_list(5, 7, 3) == 5