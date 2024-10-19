
import time

def print_separator():
	print("------------------------------")

class InputArrayGenerator:
	OPTIONS = {
		"1": "Manual Input",
		"2": "Random Array (Random Length)",
		"3": "Null Value",
		"4": "Empty Array",
		"5": "Quit",
	}
	
	def __init__():
		pass
			
	@staticmethod
	def choose_input_option():
		print('hello')
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
				return InputArrayGenerator.handle_choice(int(choice))
			except TypeError as error:
				print(error)
				return False

	@staticmethod
	def handle_choice(choice):
		print_separator()
		match choice:
			case 1:
				return InputArrayGenerator.get_manual_input()

	@staticmethod
	def get_manual_input():
		arr = input("Input Array of Numbers (Seperated by Commas): ").split(",")
		target = input("Target Value: ")
		if not target.isdigit():
			print_separator()
			raise TypeError(f"{target} is not an integer...")
		arr = [int(num) for num in arr if num.isdigit()]
		print((arr, target))
		return(arr, int(target))

	@staticmethod
	def get_random_array():
		pass

	@staticmethod
	def get_null_value():
		pass

	@staticmethod
	def get_empty_array():
		pass