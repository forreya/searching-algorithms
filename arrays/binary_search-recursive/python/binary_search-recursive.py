from input_array_generator import InputArrayGenerator

def binary_search-recursive(arr, target):
	left, right = 0, len(arr) - 1

	if len(arr) == 0:
		return False
	if len(arr) == 1:
		return arr[0] == target

	mid = left + (right - left) // 2

	if target < arr[mid]:
		return binary_search-recursive(arr[0:mid], target)
	elif target > arr[mid]:
		return binary_search-recursive(arr[mid+1:], target)
	else:
		return True

res = InputArrayGenerator.choose_input_option()
if res:
	print(f"Result: {binary_search-recursive(res[0], res[1])}")