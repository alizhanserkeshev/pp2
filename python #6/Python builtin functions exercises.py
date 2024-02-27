#task 1
from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers_list = [2, 3, 4, 5]
result = multiply_list(numbers_list)
print(f"Product of all numbers in the list: {result}")

#task 2
def count_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

input_str = "Hello World"
upper, lower = count_case_letters(input_str)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

#task 3
def is_palindrome(input_str):
    reversed_str = input_str[::-1]
    return input_str == reversed_str

input_str = "level"
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")

#task 4
import time
import math

def calculate_square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = 25100
delay_milliseconds = 2123
result = calculate_square_root_after_delay(number, delay_milliseconds)
print(f"Square root of {number} after {delay_milliseconds} milliseconds is {result}")

#task 5
def all_elements_true(input_tuple):
    return all(input_tuple)

tuple_values = (True, True, False, True)
if all_elements_true(tuple_values):
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")


