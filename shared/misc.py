def print_separator():
	print("------------------------------")

def assertIsInteger(val):
	if not val.isdigit():
		print_separator()
		raise TypeError(f"'{val}' is not an integer...")