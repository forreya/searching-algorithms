from input_array_generator import InputArrayGenerator

def binary_search_first_occurence(arr, target):
	left, right = 0, len(arr) - 1
	result = -1
	while right >= left:
		middle = left + (right - left) // 2
		if target > arr[middle]:
			left = middle + 1
		elif target < arr[middle]:
			right = middle - 1
		else:
			result = middle
			right = middle - 1 
	return result if result != -1 else False

def binary_search_last_occurence(arr, target):
	left, right = 0, len(arr) - 1
	result = -1
	while right >= left:
		middle = left + (right - left) // 2
		if target > arr[middle]:
			left = middle + 1
		elif target < arr[middle]:
			right = middle - 1
		else:
			result = middle
			left = middle + 1 
	return result if result != -1 else False

res = InputArrayGenerator.choose_input_option()
if res:
	print(f"Result of first occurence: {binary_search_first_occurence(res[0], res[1])}")
	print(f"Result of last occurence: {binary_search_last_occurence(res[0], res[1])}")
