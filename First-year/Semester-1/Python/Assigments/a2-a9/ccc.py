def can_place_horizontal(matrix, x, y):
    return y + 1 < len(matrix) and matrix[x][y] == 0 and matrix[x][y + 1] == 0


def can_place_vertical(matrix, x, y):
    return x + 1 < len(matrix) and matrix[x][y] == 0 and matrix[x + 1][y] == 0


def place_horizontal(matrix, x, y):
    matrix[x][y] = 1
    matrix[x][y + 1] = 1


def place_vertical(matrix, x, y):
    matrix[x][y] = 1
    matrix[x + 1][y] = 1


def remove_horizontal(matrix, x, y):
    matrix[x][y] = 0
    matrix[x][y + 1] = 0


def remove_vertical(matrix, x, y):
    matrix[x][y] = 0
    matrix[x + 1][y] = 0


def backtrack(matrix, count):
    max_offices = count
    best_matrix = [row[:] for row in matrix]  # Copie a matricei curente

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                # Încearcă să plasezi un birou orizontal
                if can_place_horizontal(matrix, i, j):
                    place_horizontal(matrix, i, j)
                    current_offices, current_matrix = backtrack(matrix, count + 1)
                    if current_offices > max_offices:
                        max_offices = current_offices
                        best_matrix = current_matrix
                    remove_horizontal(matrix, i, j)

                # Încearcă să plasezi un birou vertical
                if can_place_vertical(matrix, i, j):
                    place_vertical(matrix, i, j)
                    current_offices, current_matrix = backtrack(matrix, count + 1)
                    if current_offices > max_offices:
                        max_offices = current_offices
                        best_matrix = current_matrix
                    remove_vertical(matrix, i, j)

    return max_offices, best_matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    N = int(input("Introdu dimensiunea matricei pătratice (N x N): "))
    matrix = [[0] * N for _ in range(N)]  # Matricea inițială

    result, final_matrix = backtrack(matrix, 0)
    print(f"Numărul maxim de birouri: {result}")
    print("Matricea cu birourile plasate:")
    print_matrix(final_matrix)
