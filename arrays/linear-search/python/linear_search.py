from arrays.input_array_generator import InputArrayGenerator

def linear_search(arr, target):
	for number in arr:
		if number == target:
			return True
	return False


res = InputArrayGenerator.choose_input_option()
if res:
	print(linear_search(res[0], res[1]))