import re

pattern = re.compile(r'abb{2,3}')

def match_string(input_str):
    return bool(pattern.match(input_str))

# Example usage
input_str = "abbbb"
result = match_string(input_str)
print(result)  # Output: True
