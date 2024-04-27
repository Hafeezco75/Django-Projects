from stringslicing import length


def test_for_string_returns_first_and_last_characters():
	assert length("semicolon") == "seon"

def test_for_string_less_then_two():
	assert length("on", "on") == "onon"

def test_returns_empty_string():
	assert length("o") == ""