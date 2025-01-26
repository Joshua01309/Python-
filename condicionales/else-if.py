# Ejemplo de condicional if-elif-else
z = 7
if z > 10:
    print("z es mayor que 10")
elif z > 5:
    print("z es mayor que 5 pero menor o igual que 10")
else:
    print("z es menor o igual que 5")

# Con elif podemos agregar tanta condiciones como nosotros queramos

# Ejemplo de condicional anidado
a = 8
b = 6
if a > 5:
    if b > 5:
        print("a y b son mayores que 5")
    else:
        print("a es mayor que 5 pero b no lo es")
else:
    print("a no es mayor que 5")