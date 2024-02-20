import re

pattern = re.compile(r'[A-Z][a-z]+')

def find_sequences(input_str):
    return pattern.findall(input_str)

# Example usage
input_str = "CamelCase and PythonProgramming"
result = find_sequences(input_str)
print(result)  # Output: ['Camel', 'Case', 'Python', 'Programming']
