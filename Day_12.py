def min_moves_to_different_colors(n, s):
    count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
    return count

# Read input
n = int(input())
s = input()

# Calculate and print the result
result = min_moves_to_different_colors(n, s)
print(result)