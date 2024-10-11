
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
		
	def handle_choice():
		pass

	def get_manual_input():
		arr = input("Input Array of Numbers (Seperated by Commas): ").split(",")
		target = input("Target Value: ")
		return arr, target

	def get_random_array():
		pass

	def get_null_value():
		pass

	def get_empty_array():
		pass
		
InputArrayGenerator.choose_input_option()