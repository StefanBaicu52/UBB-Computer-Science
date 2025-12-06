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
        if poz == 0 or l[poz] >= l[poz - 1]:
            poz += 1
        else:
            l[poz], l[poz - 1] = l[poz - 1], l[poz]
            poz -= 1
    return l

def interpsrc(l, x):
    mic, mare = 0, len(l) - 1
    while mic <= mare and x >= l[mic] and x <= l[mare]:
        if l[mic] == l[mare]:
            return mic if l[mic] == x else -1
        pozitie = mic + (x - l[mic]) * (mare - mic) // (l[mare] - l[mic])
        if l[pozitie] == x:
            return pozitie
        elif x > l[pozitie]:
            mic = pozitie + 1
        else:
            mare = pozitie - 1
    return -1

def create_best_case(n):
    return list(range(n))

def create_worst_case(n):
    return list(range(n, 0, -1))

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

def main():
    n = 0
    gen = 0
    l = []

    while n != 8:
        n = int(input("Please select the command: \n 1: Generate a list \n 2: Sort using exchange method \n 3: Sort using gnome method \n 4: Search a number \n 5: Best case timing \n 6: Worst case timing \n 7: Average case timing \n 8: Exit: "))
        if n == 1:
            m = int(input("Enter number of elements: "))
            l = generate(m)
            gen = 1
        elif n == 4:
            if gen:
                m = int(input("Enter number to search: "))
                p = interpsrc(sorted(l), m)  # Sort the list for searching
                print(f"The number is located at position {p}" if p != -1 else "Number not found")
            else:
                print("Please generate a list first.")
        elif n == 2:
            if gen:
                l = exchange(l.copy())
                print("List sorted using Exchange sort.")
            else:
                print("Please generate a list first.")
        elif n == 3:
            if gen:
                l = gnomesort(l.copy())  # Sort a copy
                print("List sorted using Gnome sort.")
            else:
                print("Please generate a list first.")
        elif n == 5:
            sizes = [500, 1000, 2000, 4000, 8000]
            for size in sizes:
                l = create_best_case(size)
                time_taken = measure_time(exchange, l.copy())
                print(f"Best case time (Exchange Sort, size {size}): {time_taken:.6f} seconds")
                time_taken = measure_time(gnomesort, l.copy())
                print(f"Best case time (Gnome Sort, size {size}): {time_taken:.6f} seconds")
        elif n == 6:
            sizes = [500, 1000, 2000, 4000, 8000]
            for size in sizes:
                l = create_worst_case(size)




                time_taken = measure_time(exchange, l.copy())
                print(f"Worst case time (Exchange Sort, size {size}): {time_taken:.6f} seconds")
                time_taken = measure_time(gnomesort, l.copy())
                print(f"Worst case time (Gnome Sort, size {size}): {time_taken:.6f} seconds")
        elif n == 7:
            sizes = [500, 1000, 2000, 4000, 8000]
            for size in sizes:
                l = generate(size)
                time_taken = measure_time(exchange, l.copy())
                print(f"Average case time (Exchange Sort, size {size}): {time_taken:.6f} seconds")
                time_taken = measure_time(gnomesort, l.copy())
                print(f"Average case time (Gnome Sort, size {size}): {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()