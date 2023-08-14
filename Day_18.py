def string_task(s):
    vowels = "AEIOUYaeiouy"
    result = []
    for char in s:
        if char not in vowels:
            result.append('.')
            result.append(char.lower())
    return ''.join(result)

# Read input
input_string = input().strip()

# Call the function and print the result
output_string = string_task(input_string)
print(output_string)