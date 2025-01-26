def suma(a,b):
    return a+b

resultado = suma(5,3)

# agregando mas numeros, forma no optima
def suma_lista(lista):
    suma_total = 0
    for numero in lista:
        suma_total = suma_total + numero
    return suma_total

resultado = suma_lista([1,2])
print(resultado)

# forma optima
def suma(numeros):
    return sum([*numeros])
resultado = suma([1,2])
print(resultado)

# forma optima utilizando el operador como argumento (*args)
def suma(*numeros):
    return sum(numeros)
resultado = suma(1,2)
print(resultado)

def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es {sum(numeros)}'
resultado = suma('josue', 1, 2)
print(resultado)