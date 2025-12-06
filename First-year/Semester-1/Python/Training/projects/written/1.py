def f(a, b):
    b.append(a)
    a = [a]
    b = b + a
    return b

x = 1
y = [2]
z = f(x, y)
print([1] == x)  # False, since x is an integer (not a list)
print(id(y) == id(z))  # True, since b.append(a) modifies y directly
print(y == z[0:2])
print(y)
print(z)
print(z[0:2])