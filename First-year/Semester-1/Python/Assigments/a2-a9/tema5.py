import math


# Complex Number Operations
def create_complex_number_list(re, im):
    """Create a complex number in list form [real, imaginary]."""
    return [re, im]


def create_complex_number_dict(re, im):
    """Create a complex number in dictionary form {'real': real, 'imaginary': imaginary}."""
    return {"real": re, "imaginary": im}


def display_complex_number_list(cn):
    """Display a complex number in list form."""
    print(f"{cn[0]} + {cn[1]}i")


def display_complex_number_dict(cn):
    """Display a complex number in dictionary form."""
    print(f"{cn['real']} + {cn['imaginary']}i")


def modulus(cn):
    """Calculate modulus of a complex number."""
    return math.sqrt(cn[0] ** 2 + cn[1] ** 2)  # List representation


def modulus_dict(cn):
    """Calculate modulus of a complex number (using dictionary)."""
    return math.sqrt(cn['real'] ** 2 + cn['imaginary'] ** 2)  # Dictionary representation


# Functions for Set A (Naive Implementation)
def longest_subarray_with_at_most_3_distinct(cn_list):
    """Find the longest subarray with at most 3 distinct complex numbers."""
    start = 0
    max_len = 0
    result = []
    distinct_numbers = {}

    for end in range(len(cn_list)):
        cn_tuple = (cn_list[end][0], cn_list[end][1])  # Use tuple (real, imaginary) as the key
        if cn_tuple in distinct_numbers:
            distinct_numbers[cn_tuple] += 1
        else:
            distinct_numbers[cn_tuple] = 1

        while len(distinct_numbers) > 3:
            start_tuple = (cn_list[start][0], cn_list[start][1])
            distinct_numbers[start_tuple] -= 1
            if distinct_numbers[start_tuple] == 0:
                del distinct_numbers[start_tuple]
            start += 1

        if (end - start + 1) > max_len:
            max_len = end - start + 1
            result = cn_list[start:end + 1]

    return result


# Functions for Set B (Dynamic Programming Implementation)
def longest_alternating_subsequence_real(cn_list):
    """Find the longest alternating subsequence based on the real part."""
    n = len(cn_list)
    if n == 0:
        return []

    # dp[i] will store the length of the longest alternating subsequence ending at index i
    dp = [1] * n  # Each element is a subsequence by itself
    direction = [0] * n  # 1: increasing, -1: decreasing, 0: undefined

    for i in range(1, n):
        for j in range(i):
            if cn_list[i][0] > cn_list[j][0] and direction[j] != 1:
                dp[i] = dp[j] + 1
                direction[i] = 1
            elif cn_list[i][0] < cn_list[j][0] and direction[j] != -1:
                dp[i] = dp[j] + 1
                direction[i] = -1

    # Reconstruct the longest alternating subsequence
    max_len = max(dp)
    result = []
    index = dp.index(max_len)
    result.append(cn_list[index])

    # Backtrack to get the subsequence
    for i in range(index - 1, -1, -1):
        if dp[i] == dp[index] - 1 and direction[i] != direction[index]:
            result.append(cn_list[i])
            index = i

    return result[::-1]


# Input and Output Functions
def read_complex_numbers():
    """Read a list of complex numbers from the console."""
    cn_list = []
    n = int(input("How many complex numbers would you like to input? "))
    for i in range(n):
        re, im = map(float, input(f"Enter complex number {i + 1} (real imaginary): ").split())
        cn_list.append(create_complex_number_list(re, im))  # Use list representation
    return cn_list


def display_complex_numbers(cn_list):
    """Display a list of complex numbers."""
    print("Complex numbers list:")
    for cn in cn_list:
        display_complex_number_list(cn)


def main():
    complex_numbers = []  # List to hold complex numbers

    while True:
        print("\nMenu:")
        print("1. Read complex numbers")
        print("2. Display all complex numbers")
        print("3. Find longest subarray with at most 3 distinct values (Set A)")
        print("4. Find longest alternating subsequence based on real part (Set B)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            complex_numbers = read_complex_numbers()
        elif choice == '2':
            display_complex_numbers(complex_numbers)
        elif choice == '3':
            result = longest_subarray_with_at_most_3_distinct(complex_numbers)
            print("Longest subarray with at most 3 distinct complex numbers:")
            for cn in result:
                display_complex_number_list(cn)
        elif choice == '4':
            result = longest_alternating_subsequence_real(complex_numbers)
            print("Longest alternating subsequence based on real part:")
            for cn in result:
                display_complex_number_list(cn)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()
