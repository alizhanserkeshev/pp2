import re

pattern = re.compile(r'a.*b$')

def match_string(input_str):
    return bool(pattern.match(input_str))

# Example usage
input_str = "aanythingb"
result = match_string(input_str)
print(result)  # Output: True
