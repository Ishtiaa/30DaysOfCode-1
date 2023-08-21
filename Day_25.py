n = int(input())
s = input()

count_a = s.count('A')
count_d = s.count('D')

if count_a > count_d:
    print("Anton")
elif count_d > count_a:
    print("Danik")
else:
    print("Friendship")
