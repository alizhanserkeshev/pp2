import re

def split_at_uppercase(input_str):
    return re.findall('[A-Z][a-z]*', input_str)

# Example usage
input_str = "SplitAtUpperCase"
result = split_at_uppercase(input_str)
print(result)  # Output: ['Split', 'At', 'Upper', 'Case']
