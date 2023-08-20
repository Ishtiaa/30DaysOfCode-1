def is_lucky(num):
    lucky_digits = [4, 7]
    count = 0
    while num > 0:
        digit = num % 10
        if digit in lucky_digits:
            count += 1
        num //= 10
    return count in lucky_digits

def is_nearly_lucky(num):
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477]
    return is_lucky(num) or num in lucky_numbers

n = int(input().strip())
if is_nearly_lucky(n):
    print("YES")
else:
    print("NO")