import re

def camel_to_snake(camel_case):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()

# Example usage
camel_case_str = "CamelCaseString"
snake_case_str = camel_to_snake(camel_case_str)
print(snake_case_str)  # Output: camel_case_string
