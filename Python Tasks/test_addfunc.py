from addup import add

def test_add():
	assert add(3, 4) == 7
	assert add(10, 5) == 15

def test_add_strings():
	assert add("lambo", " alero") == "lambo alero"
	assert add("eniola", " job") == "eniola job"

def test_negative_values_with_add_function():
	assert add(-3, -4) == 7