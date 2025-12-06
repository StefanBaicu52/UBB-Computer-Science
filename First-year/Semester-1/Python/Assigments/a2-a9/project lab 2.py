#interpolation search
#Exchange Sort
#Gnome Sort
import random

def generate(n):
    numbers=[random.randint(0, 1000) for _ in range(n)]
    return numbers

def exchange(l,nr):
    nra=0
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
                nra+=1
            if(nra%nr==0):
                print(l)
    return l

def gnomesort(l,nr):
    poz=0
    nrr=0
    while poz<len(l):
        if poz==0 or l[poz]>l[poz-1]:
            poz+=1
        else:
            aux=l[poz]
            l[poz]=l[poz-1]
            l[poz-1]=aux
            poz-=1
            nrr+=1
            if(nrr%nr==0):
                print(l)
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

n=0
gen=0

while n!=5:
    n = int(input("Please select the command: \n 1:Generate a list with random numbers and select how many numbers would like in the list \n 2:Sort the list using exchange method \n 3:Sort the list using gnome method \n 4:Search an number using the interpolation method \n 5:Exit "))
    if(n==1):
        m=int(input("Please select how many would u like to have in the list: "))
        sor = 0
        l=generate(m)
        print(f"The list is {l}")
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
          m=int(input("Please select how often would u like to see the list while being sorted: "))
          l=exchange(l,m)
          print(f"The list is {l}")
          sor=1
        else:
          if(gen==0):
              print("Please generate a list!: ")

    if (n == 3):
        if (gen == 1):
            m = int(input("Please select how often would u like to see the list while being sorted: "))
            l=gnomesort(l, m)
            print(f"The list is {l}")

            sor = 1
        else:
            if (gen == 0):
                print("Please generate a list!: ")



