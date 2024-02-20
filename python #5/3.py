import re

pattern = re.compile(r'[a-z]+_[a-z]+')

def find_sequences(input_str):
    return pattern.findall(input_str)

# Example usage
input_str = "hello_world and python_programming"
result = find_sequences(input_str)
print(result)  # Output: ['hello_world', 'python_programming']
