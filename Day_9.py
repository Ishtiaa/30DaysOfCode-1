# Boy Or Girl
def determine_gender(user_name):
    distinct_chars = set(user_name)
    if len(distinct_chars) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

# Read input from standard input
user_name = input().strip()

# Call the function and print the result
result = determine_gender(user_name)
print(result)
