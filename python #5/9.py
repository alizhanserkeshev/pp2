import re

def insert_spaces(input_str):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', input_str)

# Example usage
input_str = "InsertSpacesBetweenWords"
result = insert_spaces(input_str)
print(result)  # Output: Insert Spaces Between Words
