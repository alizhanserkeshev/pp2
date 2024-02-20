def snake_to_camel(snake_case):
    words = snake_case.split('_')
    return ''.join(word.capitalize() for word in words)

# Example usage
snake_case_str = "my_snake_case_string"
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)  # Output: MySnakeCaseString
