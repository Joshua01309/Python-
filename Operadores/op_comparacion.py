# Operadores de comparación en Python

# Igual a
a = 5
b = 5
print(a == b)  # True

# Diferente de
c = 10
d = 5
print(c != d)  # True

# Mayor que
e = 7
f = 3
print(e > f)  # True

# Menor que
g = 2
h = 8
print(g < h)  # True

# Mayor o igual que
i = 6
j = 6
print(i >= j)  # True

# Menor o igual que
k = 4
l = 9
print(k <= l)  # True

# Nota:
# '=' es un operador de asignación que se usa para asignar un valor a una variable.
# '==' es un operador de comparación que se usa para comparar si dos valores son iguales.

a = 5
b = 7
c = 9
print( a+b >=c)
# Comparación de cadenas de texto
str1 = "Hola"
str2 = "Mundo"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 < str2)   # True (orden lexicográfico)
print(str1 > str2)   # False (orden lexicográfico)