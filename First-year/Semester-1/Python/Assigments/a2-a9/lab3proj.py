
import random
import time


def generate(n):
    return [random.randint(0, 1000) for _ in range(n)]


def exchange(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def gnomesort(l):
    poz = 0
    while poz < len(l):
        if poz == 0 or l[poz] > l[poz - 1]:
            poz += 1
        else:
            l[poz], l[poz - 1] = l[poz - 1], l[poz]
            poz -= 1
    return l


def interpsrc(l, x):
    mic = 0
    mare = len(l) - 1
    while mic <= mare and x >= l[mic] and x <= l[mare]:
        if l[mic] == l[mare]:
            if l[mic] == x:
                return mic
            return -1
        pozitie = mic + (x - l[mic]) * (mare - mic) // (l[mare] - l[mic])
        if l[pozitie] == x:
            return pozitie
        if x > l[pozitie]:
            mic = pozitie + 1
        else:
            mare = pozitie - 1
    return -1


def create_best_case(n):
    return list(range(n))  # Sorted list for best case


def create_average_case(n):
    return random.sample(range(0, 1000), n)  # Random unique list for average case


def create_worst_case(n):
    return list(range(n, 0, -1))  # Reverse sorted list for worst case


def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time


def main_menu():
    gen = False
    l = []

    while True:
        n = int(input("Please select the command: \n"
                      "1: Generate a list with random numbers\n"
                      "2: Sort the list using exchange method\n"
                      "3: Sort the list using gnome method\n"
                      "4: Search for a number using the interpolation method\n"
                      "5: Best case sorting\n"
                      "6: Average case sorting\n"
                      "7: Worst case sorting\n"
                      "8: Exit\n"))

        if n == 1:
            m = int(input("Please select how many numbers you would like in the list: "))
            l = generate(m)
            print(f"The list is: {l}")
            gen = True
        elif n in [2, 3, 5, 6, 7]:
            if not gen:
                print("Please generate a list first!")
                continue
            if n == 2:
                l=exchange(l)
                print(f"The list is: {l}")
            elif n == 3:
                l=gnomesort(l)
                print(f"The list is: {l}")
            elif n == 5:
                aux = len(l)
                while aux * 16 >= len(l):
                    time_taken = measure_time(exchange, l)
                    print(f"Time taken (Best Case Sorting Exchange): {time_taken:.6f} seconds")
                    time_taken = measure_time(gnomesort, l)
                    print(f"Time taken (Best Case Sorting Gnome): {time_taken:.6f} seconds")
                    l = generate(len(l) * 2)
            elif n == 6:
                time_taken = measure_time(lambda x: exchange(x, m), create_average_case(len(l)))
                print(f"Time taken (Average Case Sorting): {time_taken:.6f} seconds")
            elif n == 7:
                time_taken = measure_time(lambda x: exchange(x, m), create_worst_case(len(l)))
                print(f"Time taken (Worst Case Sorting): {time_taken:.6f} seconds")
        elif n == 4:
            if not gen:
                print("Please generate a list first!")
                continue
            m = int(input("Please select what number you would like to search for: "))
            p = interpsrc(sorted(l), m)  # Ensure the list is sorted before searching
            if p == -1:
                print("Sorry, that number is not in the list.")
            else:
                print(f"The number is located at position {p}.")
        elif n == 8:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()