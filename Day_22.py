def is_dangerous(situation):
    consecutive_count = 1
    for i in range(1, len(situation)):
        if situation[i] == situation[i - 1]:
            consecutive_count += 1
            if consecutive_count >= 7:
                return "YES"
        else:
            consecutive_count = 1
    return "NO"
situation = input().strip()
result = is_dangerous(situation)
print(result)





