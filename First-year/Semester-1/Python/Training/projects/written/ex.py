class SparseList:
    def _init_(self):
        self.data=[]

    def _setitem_(self, key, value):
        for i in range(key):
            if self.data[i]==' ':
                self.data[i]=0
        self.data[key]=value

    def _getitem_(self, key):
        return self.data[key]

    def _iter_(self):
        return SparceListIterator(self)

class SparceListIterator:
    def _init_(self, sparse_list):
        self.sparse_list = sparse_list
        self.current_index = 0
        self.max_index = sparse_list.data[-1][0] if sparse_list.data else -1  # Ultimul index setat

    def _iter_(self):
        return self

    def _next_(self):
        if self.current_index > self.max_index:
            raise StopIteration
        value = self.sparse_list[self.current_index]
        index = self.current_index
        self.current_index += 1
        return index, value




ex 3 aia cu random:import random


def test_f():
    # Generate 100 random lists
    for _ in range(100):
        # Randomly decide the length of the list (1 to 20 elements)
        length = random.randint(1, 20)

        # Generate a random list of integers between -50 and 50
        data = [random.randint(-50, 50) for _ in range(length)]

        # Test the function f with the generated list
        try:
            result = f(data)

            # Check if f behaves as expected
            if result:
                # If f(data) is True, confirm the list is sorted
                assert data == sorted(data), f"Test failed: {data} marked as sorted"
            else:
                # If f(data) is False, confirm the list is not sorted
                assert data != sorted(data), f"Test failed: {data} marked as not sorted"

        except ValueError:
            # Ensure it raises a ValueError for None or empty input
            assert data is None or data == [], f"Test failed: Unexpected ValueError for {data}"

    print("All tests passed!")


# Example call to the test function
test_f()



from math import sqrt
class PrimeListException(Exception):
    """Custom exception for PrimeList."""
    pass


class PrimeList:
    def _init_(self):
        self.primes = []  # Store primes dynamically


    def _getitem_(self, index):
        # Calculate primes up to the required index
        while len(self.primes) <= index:
            self._generate_next_prime()
        return self.primes[index]

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # range -> start with 3 then +2 at every step until sqrt(n) + 1
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def _generate_next_prime(self):
        """Găsește și adaugă următorul număr prim în listă."""

        # Stabilim de unde începem căutarea următorului număr prim
        if not self.primes:
            candidate = 2  # Dacă lista e goală, primul număr prim este 2
        else:
            candidate = self.primes[-1] + 1  # Începem căutarea de la ultimul număr prim +1

        # Căutăm următorul număr prim
        while not self._is_prime(candidate):
            candidate += 1  # Incrementăm până găsim un număr prim

        # Adăugăm numărul prim în listă
        self.primes.append(candidate)


    def _setitem_(self, index, value):
        raise PrimeListException("List is read only")



#----------------------------------------------------------


class PrimeListException(Exception):
    """Custom exception for PrimeList."""
    pass


class PrimeList:
    def _init_(self):
        self.primes = {}  # Folosim un dicționar pentru a stoca primele

    def _getitem_(self, index):
        # Verificăm dacă avem deja numărul prim la indexul respectiv
        if index in self.primes:
            return self.primes[index]

        # Dacă nu avem, generăm până ajungem la indexul dorit
        while len(self.primes) <= index:
            self._generate_next_prime()

        return self.primes[index]

    @staticmethod
    def _is_prime(n):
        """Verifică dacă un număr este prim."""
        if n < 2:
            return False  # Numerele mai mici decât 2 nu sunt prime
        if n == 2:
            return True  # 2 este prim
        if n % 2 == 0:
            return False  # Oricare alt număr par nu este prim

        limit = int(n ** 0.5) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False
        return True

    def _generate_next_prime(self):
        """Găsește și adaugă următorul număr prim în dicționar."""
        # Stabilim de unde începem căutarea următorului număr prim
        if not self.primes:
            candidate = 2  # Dacă dicționarul e gol, primul număr prim este 2
        else:
            candidate = max(self.primes.keys()) + 1  # Începem de la ultimul index + 1

        # Căutăm următorul număr prim
        while not self._is_prime(candidate):
            candidate += 1  # Incrementăm până găsim un număr prim

        # Adăugăm numărul prim în dicționar
        self.primes[len(self.primes)] = candidate

    def _setitem_(self, key, value):
        raise PrimeListException("List is read only")


# Testăm cu dicționar:
prime_list = PrimeList()

print(prime_list[0])  # Ar trebui să returneze 2
print(prime_list[1])  # Ar trebui să returneze 3
print(prime_list[5])  # Ar trebui să returneze 17



class SparseMatrix:
    def _init_(self, rows, cols):
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")
        self.rows = rows
        self.cols = cols
        # Inițializăm matricea completă cu 0
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set(self, row, col, value):
        # Verificăm dacă indexul este în afara limitelor
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("Index out of bounds.")
        self.data[row][col] = value

    def get(self, row, col):
        # Verificăm dacă indexul este în afara limitelor
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("Index out of bounds.")
        return self.data[row][col]

    def _str_(self):
        # Construim o reprezentare sub formă de matrice
        result = []
        for row in self.data:
            result.append(" ".join(map(str, row)))
        return "\n".join(result)


# Testare
m1 = SparseMatrix(3, 3)
m1.set(1, 1, 2)  # Valoare la [1, 1] este 2
m1.set(1, 2, 3)  # Valoare la [1, 2] este 3
m1.set(2, 2, 4)  # Valoare la [2, 2] este 4
print(m1)        # Afișează matricea
# 0 0 0
# 0 2 3
# 0 0 4

try:
    m1.set(3, 3, 99)  # Index invalid
except Exception as e:
    print(type(e))  # Afișează eroarea: <class 'ValueError'>

m1.set(1, 1, m1.get(1, 1) + 1)  # Actualizare valoare la [1, 1]: 2 + 1 = 3
print(m1)
# 0 0 0
# 0 3 3
# 0 0 4



#------------------------------------ matrice fibbo



class FibMatrix:
    def _init_(self, n):
        """Initializează o matrice n x n de Fibonacci."""
        if n <= 0:
            raise ValueError("Matrix size must be a positive integer.")
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self._populate_matrix()

    def _fib_at_index(self, k):
        """Calculează al k-lea număr Fibonacci iterativ, folosind O(1) spațiu."""
        if k == 0:
            return 0
        elif k == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, k + 1):
            a, b = b, a + b
        return b

    def _populate_matrix(self):
        """Populează matricea cu numerele Fibonacci."""
        for i in range(self.n):
            for j in range(self.n):
                index = i * self.n + j  # Determină indexul Fibonacci bazat pe poziția în matrice
                self.matrix[i][j] = self._fib_at_index(index)

    def _str_(self):
        """Construiește o reprezentare textuală a matricei."""
        result = []
        for row in self.matrix:
            result.append(" ".join(map(str, row)))
        return "\n".join(result)

    def _add_(self, other):
        """Adună două matrice Fibonacci element cu element."""
        if self.n != other.n:
            raise ValueError("Matrices must be the same size to add.")

        result = FibMatrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def _iter_(self):
        """Iterează prin toate elementele matricei, linie cu linie."""
        for row in self.matrix:
            for value in row:
                yield value


#-------------------------------- sparce list
print("/n/n/n/n/")




#2
class SparseList:
    def _init_(self):
        self.data = []  # Stocăm doar valorile nenule ca (index, valoare)

    def _setitem_(self, index, value):
        for i, (idx, val) in enumerate(self.data):
            if idx == index:
                if value != 0:
                    self.data[i] = (index, value)  # Actualizare valoare
                else:
                    self.data.pop(i)  # Eliminare dacă e 0
                return
        if value != 0:
            self.data.append((index, value))  # Adăugare nouă pereche
            self.data.sort()  # Menținem lista sortată după index

    def _getitem_(self, index):
        for idx, val in self.data:
            if idx == index:
                return val
        return 0  # Dacă nu există, returnează 0

    def _iter_(self):
        return SparseListIterator(self)

class SparseListIterator:
    def _init_(self, sparse_list):
        self.sparse_list = sparse_list
        self.current_index = 0
        self.max_index = sparse_list.data[-1][0] if sparse_list.data else -1  # Ultimul index setat

    def _iter_(self):
        return self

    def _next_(self):
        if self.current_index > self.max_index:
            raise StopIteration
        value = self.sparse_list[self.current_index]
        index = self.current_index
        self.current_index += 1
        return index, value

# Exemplu de utilizare:
data = SparseList()
data[0] = 1
data[2] = 2

for iter1, iter2 in data:
    print(iter1, iter2)




#sparcelist exemplu 6

class SparseList:
    def _init_(self):
        self.data = []

    def set(self, index, value):
        # Asigurăm dimensiunea listei suficiente pentru indexul cerut
        while len(self.data) <= index:
            self.data.append(0)  # Adăugăm zerouri în locurile lipsă
        # Setăm valoarea
        self.data[index] = value

    def get(self, index, default=0):
        # Returnăm valoarea de la index, sau default dacă indexul e în afara limitei
        if index < len(self.data):
            return self.data[index]
        return default

    def _len_(self):
        return len(self.data)

    def _iter_(self):
        self._index = 0
        return self

    def _next_(self):
        if self._index < len(self.data):
            val = self.data[self._index]
            self._index += 1
            return val
        raise StopIteration()

# Exemplu de utilizare:
data = SparseList()
data.set(1, 2)  # Setăm elementul de la index 1 la 2
data.set(3, 3)  # Setăm elementul de la index 3 la 3
data.set(5, 99)  # Setăm elementul de la index 5 la 99
data.set(9, data.get(9) + 1)  # Setăm elementul de la index 9 la 1 (presupunând inițial 0)

for elem in data:
    print(elem)  # Iterăm peste toate elementele din listă









#s.index(x[, i[, j]]) index of the first occurrence of x in s (at or after index i and before index j)
#s.count(x) total number of occurrences of x in s

#list[start, end]
#Asta înseamnă că Python va extrage elementele din listă începând de la indexul start și până la indexul end exclusiv.
# Adică elementul aflat pe poziția end nu va fi inclus în rezultat.

'''
lists = [[]] * 3
lists
[[], [], []]
lists[0].append(3)
lists
[[3], [3], [3]]
'''
#=----------------

'''
range( START, STOP , STEP )
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
list(range(0, 10, 3))
[0, 3, 6, 9]
list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0))
[]
list(range(1, 0))
[]
'''
#=----------------
'''
'1,2,3'.split(',')
['1', '2', '3']
'1,2,3'.split(',', maxsplit=1)
['1', '2,3']
'1,2,,3,'.split(',')
['1', '2', '', '3', '']
'1<>2<>3<4'.split('<>')
['1', '2', '3<4']
'''
#=----------------




"""
    List
"""

myList = [1, 2, 3]
print(myList)

print(myList[1])

print('The list has', len(myList), 'elements')
print('Tha first element is', myList[0], 'and the last one is', myList[len(myList) - 1])

x = myList
print(myList, x)

"""
    What happens here?
"""
x[1] = '?'
print(myList, x)

"""
    List slicing
"""
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList[:2])     #[1, 2]
print(myList[2:])    #[3, 4, 5, 6, 7, 8, 9, 10]
myList[5:] = ['a', 'b', 'c']     #[1, 2, 3, 4, 5, 'a', 'b', 'c']
print(myList)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList[1:9] = 'x'      #[1, 'x', 10]
print(myList)

"""
    Tuple
"""
tup = 1, 2, 'a'
print(tup)
print(tup[1])

for e in tup:
    print(e)

"""
    What happens if we uncomment this line?
"""
# tup[1] = 'x'

"""
    Dictionary
"""
d = {'num': 1, 'den': 2}
print(d)

print(d['num'])
d['num'] = 99
print(d['num'])

if 'num' in d:
    print('We have num!')

del d['num']

if 'num' in d:
    print('We have num!')

fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit_list[2:])
'''
'''
'''
    https://www.stationx.net/python-data-structures-cheat-sheet/
'''
'''
    fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Accesăm primul element
print(fruit_list[0])  # "apple"

# Accesăm al doilea element
print(fruit_list[1])  # "banana"

# Accesăm ultimul element
print(fruit_list[-1])  # "mango"

# Accesăm o secvență de elemente
print(fruit_list[2:5])  # ["cherry", "orange", "kiwi"]
-> extrage elementele începând de la indexul 2 până la indexul 5, dar indexul de sfârșit este exclus

# Accesăm elementele de la început până la indexul 4 exclusiv
print(fruit_list[:4])  # ["apple", "banana", "cherry", "orange"]

# Accesăm elementele de la indexul 2 până la sfârșit
print(fruit_list[2:])  # ["cherry", "orange", "kiwi", "melon", "mango"]

# Accesăm elementele folosind indici negativi
print(fruit_list[-4:-1])  # ["orange", "kiwi", "melon"]

print(fruit_list[6:1:-2])  # ["mango", "kiwi", "cherry"]
print(fruit_list[-5:-1])  # ["orange", "kiwi", "melon"]
print(fruit_list[3:])  # ["orange", "kiwi", "melon", "mango"]

# Verificăm dacă "apple" există în listă
if "apple" in fruit_list:
    print("Yes, we have 'apple'")  # Se va afișa acest mesaj

print(fruit_list[:])  # ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
Fără start și end: Înseamnă că alegi întreaga listă.

print(fruit_list[::-2])  # ["mango", "kiwi", "orange", "apple"]
Fără start și end: Alege întreaga listă.
step = -2: Parcurge lista în ordine inversă, alegând fiecare al doilea element.
Așadar, secvența returnată va fi: ["mango", "kiwi", "orange", "apple"].

#-------------

nested_list = [["apple", "banana"], ["cherry", "orange"], ["kiwi", "melon"], ["mango"]]
print(nested_list[1][1])  # "orange"
nested_list = [["apple", "banana"], ["cherry", "orange"], ["kiwi", "melon"], ["mango"]]
print(nested_list[2][::-1])  # ["melon", "kiwi"]

'''
#=------------------------
class X:
    def f(self):
        print("X")

class Y(X):
    def _init_(self,a):
        self.__a=a
    def f(self):
        print("Y")
        self.__a.f()

class Z(Y):
    def _init_(self,a):
        super()._init_(a)

for o in (Y(Y(X()))),Z(Y(X())):
    o.f()



#---------------------
class A:
    def f(self):
        print("A")

class B(A):
    def _init_(self, obj):
        self.obj = obj

    def f(self):
        print("B")
        self.obj.f()

class C(B):
    def _init_(self, obj):
        super()._init_(obj)

for obj in (B(A()), B(B(A()))):
    obj.f()


#-----------------------------------------------------------

class A:
    def f(self):
        print("A - f()")
        self.g()  # Apel către g() din A

    def g(self):
        print("A - g()")
        self.h()  # Apel către h() din A

    def h(self):
        print("A - h()")
        self.i()  # Apel către i() din A

    def i(self):
        print("A - i()")

class B:
    def _init_(self, obj):
        self.obj = obj

    def f(self):
        print("B - f()")
        self.obj.f()  # Apel către f() pe obiectul B

    def g(self):
        print("B - g()")
        self.f()  # Apel recursiv către f() din B

class C:
    def _init_(self, obj):
        self.obj = obj

    def f(self):
        print("C - f()")
        self.obj.f()  # Apel către f() pe obiectul C

    def g(self):
        print("C - g()")
        self.obj.g()  # Apel către g() pe obiectul C

    def h(self):
        print("C - h()")
        self.obj.h()  # Apel către h() pe obiectul C


# Creăm un lanț de instanțe: C(B(A()))
obj = C(B(A()))

# Apelăm f() pe obiectul C(B(A()))
obj.f()

#----------------------------------------

class Shape:
    def _init_(self, color):
        # print("building a shape")
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def area(self):
        return 0

    def _str_(self):
        return "a " + self.color + " shape"


class Rectangle(Shape):
    def _init_(self, width, height, color):
        Shape._init_(self, color)
        # print("building a rectangle")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    def _str_(self):
        return "a " + self.color + " rectangle"


class Square(Rectangle):
    def _init_(self, side, color):
        # print("building a square")
        Rectangle._init_(self, side, side, color)

    @property
    def side(self):
        return self._width

    def _str_(self):
        return "a " + self.color + " square"


class Ellipse(Shape):
    def _init_(self, major, minor, color):
        Shape._init_(self, color)
        # print("building an ellipse")
        self._major = major
        self._minor = minor

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def area(self):
        return 3.14 * self._minor * self._major

    def _str_(self):
        return "a " + self.color + " ellipse"


class Circle(Ellipse):
    def _init_(self, radius, color):
        Ellipse._init_(self, radius, radius, color)
        # print("building a circle")

    @property
    def radius(self):
        return self.major

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    def _str_(self):
        return "a " + self.color + " circle"


if _name_ == "_main_":
    shape = Shape("red")
    print(str(shape) + ", area is = " + str(shape.area))

    """
        The rectangle 'is a' shape
    """
    rectangle = Rectangle(5, 2, "blue")
    print(str(rectangle) + ", area is = " + str(rectangle.area))

    """
        The square 'is a' particular rectangle
    """
    square = Square(3, "green")
    print(str(square) + ", area is =" + str(square.area))

    ellipse = Ellipse(10, 6, "pink")
    print(str(ellipse) + ", area is =" + str(ellipse.area))

    """
        The circle 'is a' particular ellipse
    """
    circle = Circle(8, "magenta")
    print(str(circle) + ", area is =" + str(circle.area))


    a = 1
    b = [str(a), 1]
    c = {a: a, str(b[0]): b}
    print(type(a) == type(c[1]))
    a = ['1']
    print(type(a) == type(c[1]))
    print(type(a) == type(b[0]))
    print(str(a))
    print(str(a) in c)
#-------------------
    def f(n):
        s=0
        for i in range(1,n*n+1):
            j=1
            while j<n:
                s=s+j
                j=j*2
        return s

#rezolvare
'''
def f(n):
    s = 0
    # Bucla for se execută de n^2 ori, deci complexitatea acesteia este O(n^2)
    for i in range(1, n*n + 1):  # O(n^2)
        j = 1
        # Bucla while se execută de aproximativ log2(n) ori,
        # deoarece j începe de la 1 și este înmulțit cu 2 la fiecare iterație.
        # Complexitatea acestei bucle este O(log n)
        while j < n:  # O(log n)
            s = s + j
            j = j * 2  # creșterea exponențială a lui j
    # Complexitatea totală este O(n^2) * O(log n) = O(n^2 log n)
    return s

'''




def g(f, n):
    if n == 0:
        return f() + "0"
    if type(f) == str:
        return f
    return f() + " " + g(f, n - 1)

def f():
    return "f"

print(g(g(f, 2), 3))
