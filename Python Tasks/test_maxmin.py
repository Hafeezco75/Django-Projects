from defindmaxmin import find_maximum

def test_find_maximum(8,4,9,2,5,7,3):
	assert find_maximum(8, 4, 9, 2, 5, 7, 3) == 9

from defindmaxmin import find_minimum

def test_find_minimum():
	assert find_minimum(8, 4, 9, 2, 5, 7, 3) == 2