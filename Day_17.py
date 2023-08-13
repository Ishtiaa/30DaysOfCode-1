def compare_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Read input strings
string1 = input()
string2 = input()

# Compare the strings and print the result
result = compare_strings(string1, string2)
print(result)