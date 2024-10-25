from arrays.input_array_generator import InputArrayGenerator

def binary_search_iterative(arr, target):
	left, right = 0, len(arr)-1
	while left <= right:
		mid = left + (right - left) // 2
		if target == arr[mid]:
			return True
		elif target < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return False

res = InputArrayGenerator.choose_input_option()
if res:
	print(f"Result: {binary_search_iterative(res[0], res[1])}")