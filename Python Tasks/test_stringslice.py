from stringsliceodd import len

def test_len():
	assert len("semicolon") == "eioo"

def test_for_length_with_ing():
	assert len("abc", "ing") == "abcing"