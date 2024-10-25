
import time
import random
from shared.print_seperator import print_separator

def assertIsInteger(val):
	if not val.isdigit():
		print_separator()
		raise TypeError(f"'{val}' is not an integer...")

class InputArrayGenerator:
	OPTIONS = {
		"1": "Manual Input",
		"2": "Random Array (Random Length)",
		"3": "Sorted Array (Random Length)",
		"4": "Null Value",
		"5": "Empty Array",
		"6": "Quit",
	}
	
	def __init__():
		pass
			
	@staticmethod
	def choose_input_option():
		print_separator()
		print("Please select an input method:")
		for key, val in InputArrayGenerator.OPTIONS.items():
			print(f"{key}. {val}")
		print_separator()
		choice = input("Enter: ")
		if choice not in InputArrayGenerator.OPTIONS.keys():
			option_keys = list(InputArrayGenerator.OPTIONS.keys())
			print_separator()
			print(f"Please input a number between {option_keys[0]}-{option_keys[-1]}...")
			time.sleep(1)
			InputArrayGenerator.choose_input_option()
		else:
			try:
				ret = InputArrayGenerator.handle_choice(int(choice))
				print_separator()
				print(f"Input array: {str(ret[0])}")
				print(f"Target value: {str(ret[1])}")
				return ret
			except TypeError as error:
				print(error)
				return False

	@staticmethod
	def handle_choice(choice):
		print_separator()
		match choice:
			case 1:
				return InputArrayGenerator.get_manual_input()
			case 3:
				return InputArrayGenerator.get_random_sorted_array()

	@staticmethod
	def get_manual_input():
		arr = input("Input array of numbers (seperated by commas): ").split(",")
		target = input("Target value: ")
		assertIsInteger(target)
		arr = [int(num) for num in arr if num.isdigit()]
		return(arr, int(target))

	@staticmethod
	def get_random_array():
		pass
	
	@staticmethod
	def get_random_sorted_array():
		length = input("Array length? ")
		assertIsInteger(length)
		sorted_array = sorted([random.randint(0,500) for i in range(int(length))])
		print(f"Array generated: {sorted_array}")
		doesTargetValExist = input("Would you like to have the target value exist within the array? (y/n)").lower()
		if (doesTargetValExist == "y" or doesTargetValExist == "yes"):
			target = random.choice(sorted_array)
		else:
			target = random.choice([x for x in range(500) if x not in sorted_array])
		return(sorted_array, target)

	@staticmethod
	def get_null_value():
		pass

	@staticmethod
	def get_empty_array():
		pass