def calculate_minimum_capacity(n, stops):
    capacity = 0
    current_passengers = 0
    for i in range(n):
        exiting, entering = stops[i]
        current_passengers = current_passengers - exiting + entering
        capacity = max(capacity, current_passengers)
    return capacity
n = int(input())
stops = []
for _ in range(n):
    a, b = map(int, input().split())
    stops.append((a, b))
result = calculate_minimum_capacity(n, stops)
print(result)