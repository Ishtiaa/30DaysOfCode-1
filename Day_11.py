#A. Elephant
def min_steps_to_friend_house(x):
    steps = x // 5 + (1 if x % 5 != 0 else 0)
    return steps
x = int(input())
print(min_steps_to_friend_house(x))