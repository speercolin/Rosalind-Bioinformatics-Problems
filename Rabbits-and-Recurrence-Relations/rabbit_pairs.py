# Recursive Fibonacci function for rabbits
def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)


# Number of months
n = 32

# Number of offspring produced by each pair of rabbits
k = 5

# Recursive function call
total_pairs = rabbit_pairs(n, k)

print(total_pairs)
