import re

pattern = re.compile(r'[ ,.]')

def replace_chars(input_str):
    return pattern.sub(':', input_str)

# Example usage
input_str = "Hello, world. How are you today?"
result = replace_chars(input_str)
print(result)  # Output: Hello:world:How:are:you:today:
