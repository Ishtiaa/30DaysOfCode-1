#A. Theatre Square

n, m, a = map(int, input().split())

# Calculate the number of flagstones needed for each dimension
horizontal_flagstones = (n + a - 1) // a
vertical_flagstones = (m + a - 1) // a

# Calculate the total number of flagstones needed
total_flagstones = horizontal_flagstones * vertical_flagstones

print(total_flagstones)