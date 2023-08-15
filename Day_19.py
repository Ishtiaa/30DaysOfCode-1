def borrow_amount(k, n, w):
    total_cost = 0
    for i in range(1, w + 1):
        total_cost += i * k
    
    borrow = max(0, total_cost - n)
    return borrow

# Read input values
k, n, w = map(int, input().split())

# Calculate and print the amount to borrow
borrow = borrow_amount(k, n, w)
print(borrow)