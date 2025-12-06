#we need to use data structure vector/matrice
#trebuie sa o printam
#sa explicam
def maximize_expression(A):
    n = len(A)
    max_value = float('-inf')
    best_expression = ""

    for m in range(3, n):           # m can start from index 3
        for n_index in range(2, m):  # n must be less than m
            for p in range(1, n_index):  # p must be less than n
                for q in range(0, p):   # q must be less than p
                    value = A[m] - A[n_index] + A[p] - A[q]
                    if value > max_value:
                        max_value = value
                        best_expression = f"A[{m}] - A[{n_index}] + A[{p}] - A[{q}]"

    return max_value, best_expression

# Example usage
A = [30, 5, 15, 18, 30, 40]
max_value, best_expression = maximize_expression(A)
print("Maximum Value:", max_value)
print("Expression:", best_expression)