from itertools import combinations, product
import numpy as np


def is_linearly_independent(vectors):
    """Check if a set of vectors is linearly independent over Z2."""
    matrix = np.array(vectors, dtype=int)
    n_rows, n_cols = matrix.shape
    rank = 0

    for col in range(n_cols):
        # Find a pivot row
        pivot_row = None
        for row in range(rank, n_rows):
            if matrix[row, col] % 2 == 1:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        # Swap rows if pivot_row is below the current rank
        if pivot_row != rank:
            matrix[[rank, pivot_row]] = matrix[[pivot_row, rank]]

        # Eliminate entries below the pivot
        for row in range(rank + 1, n_rows):
            if matrix[row, col] % 2 == 1:
                matrix[row] = (matrix[row] + matrix[rank]) % 2

        rank += 1

    return rank == len(vectors)


def generate_vector_space(n):
    """Generate all vectors in Z2^n."""
    return [tuple(v) for v in product([0, 1], repeat=n)]


def row_reduce_mod_2(matrix):
    """Reduce a binary matrix to row echelon form modulo 2."""
    matrix = matrix.copy()
    n_rows, n_cols = matrix.shape
    rank = 0

    for col in range(n_cols):
        # Find a pivot row
        pivot_row = None
        for row in range(rank, n_rows):
            if matrix[row, col] % 2 == 1:
                pivot_row = row
                break

        if pivot_row is None:  # No pivot in this column
            continue

        # Swap rows if pivot_row is below the current rank
        if pivot_row != rank:
            matrix[[rank, pivot_row]] = matrix[[pivot_row, rank]]

        # Eliminate entries below and above the pivot
        for row in range(n_rows):
            if row != rank and matrix[row, col] % 2 == 1:
                matrix[row] = (matrix[row] + matrix[rank]) % 2

        rank += 1

    return matrix


def canonicalize_basis(basis):
    """Convert a basis to a canonical form by row reducing it."""
    matrix = np.array(basis, dtype=int)
    reduced_matrix = row_reduce_mod_2(matrix)
    # Sort rows lexicographically for consistency
    sorted_rows = tuple(sorted(map(tuple, reduced_matrix)))
    return sorted_rows


def k_dimensional_subspaces(k, n):
    """Find all k-dimensional subspaces and their bases."""
    vector_space = generate_vector_space(n)
    subspaces = set()  # Use a set to store unique subspaces

    for subset in combinations(vector_space, k):
        # Check if the vectors in the subset form a basis
        if is_linearly_independent(subset):
            # Canonicalize the basis and add to the set
            canonical_basis = canonicalize_basis(subset)
            subspaces.add(canonical_basis)

    return subspaces


def main():
    # Input: k and n
    k = int(input("Enter the dimension of subspace (k): "))
    n = int(input("Enter the dimension of the ambient space (n): "))

    if k > n:
        print("k must be less than or equal to n.")
        return

    # Find all k-dimensional subspaces
    subspaces = k_dimensional_subspaces(k, n)

    # Output the result
    print(f"The number of {k}-dimensional subspaces is: {len(subspaces)}")
    print("A basis for each subspace:")
    for basis in subspaces:
        # Convert numpy types to Python integers for clean printing
        clean_basis = [tuple(map(int, vector)) for vector in basis]
        print(clean_basis)


if __name__ == "__main__":
    main()
