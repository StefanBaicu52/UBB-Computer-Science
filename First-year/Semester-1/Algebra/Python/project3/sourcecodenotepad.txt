from itertools import combinations

# function to generate all binary vectors of length n
def generate_vectors(n):
    return [[(i >> j) & 1 for j in range(n)] for i in range(1 << n)]

# function to check if a set of vectors is linearly independent
def is_linearly_independent(basis):
    n = len(basis)
    matrix = [row[:] for row in basis]

    # Gaussian elimination over Z2
    for i in range(n):
        if matrix[i][i] == 0:
            found = False
            for j in range(i + 1, n):
                if matrix[j][i] == 1:
                    matrix[i], matrix[j] = matrix[j], matrix[i]  # Swap rows
                    found = True
                    break
            if not found:
                return False  # no pivot found

        for j in range(i + 1, n):
            if matrix[j][i] == 1:
                matrix[j] = [(matrix[j][k] ^ matrix[i][k]) for k in range(n)]  # Row operation

    return True

# function to find all bases of the vector space Z2^n
def find_bases(vectors, n):
    bases = []
    for basis in combinations(vectors, n):
        if is_linearly_independent(basis):
            bases.append(basis)
    return bases

# Function to calculate the number of bases for Z2^n
def calculate_number_of_bases(n):
    product = 1
    for k in range(n):
        product *= (2**n - 2**k)
    return product

# Main function
def main():
    n = int(input("Please type here the value of n : "))
    if n <= 0:
        print("Invalid input. Please enter a positive value of n.")
        return

    # Calculate the number of bases
    number_of_bases = calculate_number_of_bases(n)
    print(f"Number of bases for Z2^{n} over Z2 is: {number_of_bases}")

    if n < 5:
        vectors = generate_vectors(n)
        bases = find_bases(vectors, n)
        print(f"The vectors of each basis are:")
        for basis in bases:
            print(", ".join(str(tuple(vec)) for vec in basis))

if __name__ == "__main__":
    main()
