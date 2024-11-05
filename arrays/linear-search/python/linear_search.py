from arrays.input_array_generator import InputArrayGenerator

def linear_search(arr, target) -> bool:
	for number in arr:
		if number == target:
			return True
	return False


res = InputArrayGenerator.choose_input_option()
if res:
	print(f"Result: {linear_search(res[0], res[1])}")