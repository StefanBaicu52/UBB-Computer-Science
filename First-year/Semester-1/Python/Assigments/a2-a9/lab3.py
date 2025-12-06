#teoretical analyze time complexity of sorting/ search
#best/worst case  and say it and write it

#Add 3 options of the project lab 2
#6 worst case
#7 best case
#8 average
#generate 5 lists 500 1000 2000 4000 8000 they need to double in size
#preper the list for the best and worst case
#    sort the list while time it (" timeit,time") functii de timp
#    count how much time it takes
#u dont print while sorted
#u dont have to show the list


import random
import time


def generate(n):
    numbers=[random.randint(0, 1000) for _ in range(n)]
    return numbers[:]

def exchange(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
    return l

def gnomesort(l):
    poz=0
    while poz<len(l):
        if poz==0 or l[poz]>l[poz-1]:
            poz+=1
        else:
            aux=l[poz]
            l[poz]=l[poz-1]
            l[poz-1]=aux
            poz-=1
    return l

def interpsrc(l,x):
    mic=0
    mare=len(l)-1
    while mic<=mare and x>=l[mic] and x<=l[mare]:
        if l[mic]==l[mare]:
            if(l[mic]==x):
                return mic
            return -1
        pozitie=mic+(x-l[mic])*(mare-mic)//(l[mare]-l[mic])
        if(l[pozitie]==x):
            return pozitie
        if(x>l[pozitie]):
            mic=pozitie+1
        if(x<l[pozitie]):
            mare=pozitie-1
    return -1

def create_best_case(n):
    return list(range(n))

def create_worst_case(n):
    return list(range(n, 0, -1))  # Reverse sorted list for worst case


def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

n=0
gen=0

while n!=8:
    n = int(input("Please select the command: \n 1:Generate a list with random numbers and select how many numbers would like in the list \n 2:Sort the list using exchange method \n 3:Sort the list using gnome method \n 4:Search an number using the interpolation method \n 5:Best case \n 6:Worst case \n 7:average case \n 8:Exit: "))
    if(n==1):
        m=int(input("Please select how many numebrs would u like to have in the list: "))
        sor = 0
        l=generate(m)
        gen=1
    if(n==4):
        if(sor==1):
          m=int(input("Please select what number would u like to search: "))
          p=interpsrc(l,m)
          if(p==-1):
              print("Sorry that number is not in the list")
          else:
              print(f"The number is located in pozition {p}")
        else:
            print("Please sort the list first")
    if(n==2):
        if(gen==1):
          l=exchange(l)
          sor=1
        else:
          if(gen==0):
              print("Please generate a list!: ")
    if (n == 3):
        if (gen == 1):
            l=gnomesort(l)
            sor = 1
        else:
            if (gen == 0):
                print("Please generate a list!: ")
    if(n==5):
        sizes=[100,200,400,800,1600,3200,6400]
        for size in sizes:
            l=generate(size)
            l.sort()
            time_taken = measure_time(exchange, l)
            print(f"Time taken (Best Case Sorting Exchange): {time_taken:.6f} seconds")
            time_taken = measure_time(gnomesort, l)
            print(f"Time taken (Best Case Sorting Gnome): {time_taken:.6f} seconds")
    if (n == 6):
        aux = len(l)
        while aux * 16 >= len(l):
            l.sort(reverse=True)
            time_taken = measure_time(exchange, l)
            print(f"Time taken (Worst Case Sorting Exchange): {time_taken:.6f} seconds")
            time_taken = measure_time(gnomesort, l)
            print(f"Time taken (Worst Case Sorting Gnome): {time_taken:.6f} seconds")
            l = generate(len(l) * 2)
    if (n == 7):
        aux = len(l)
        while aux * 16 >= len(l):
            time_taken = measure_time(exchange, l)
            print(f"Time taken (Average Case Sorting Exchange): {time_taken:.6f} seconds")
            time_taken = measure_time(gnomesort, l)
            print(f"Time taken (Average Case Sorting Gnome): {time_taken:.6f} seconds")
            l = generate(len(l) * 2)






