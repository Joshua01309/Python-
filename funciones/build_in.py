# una funcion es un fragemnto de codigo que se puede ejectutar en cualquier otra parte o moento
# sin tener que rescribir el codigo una y otra vez

# encontrar el numero mas alto de una lista
numero = [4, 8, 15, 16, 23, 42]
mas_alto = max(numero)
print(mas_alto)

# encontar el numero mas pequeño
mas_bajo = min(numero)
print(mas_bajo)

# redondear numeros flotantes
redondeo = round(12.14255, 2)
print(redondeo)

# La función bool() en Python se utiliza para convertir un valor a su valor 
# booleano correspondiente, es decir, True o False. Esta función es útil 
# para evaluar la "verdad" de un valor en contextos donde se necesita una evaluación booleana. 
# retorna false --> 0, vacio, false, none  / True -> distinto a 0, True , cadena, datos no vacios 
boleano = bool()

# La función all() en Python se utiliza para verificar si todos los elementos de un iterable 
# (como una lista, tupla, conjunto, etc.) son verdaderos. Devuelve True si todos los elementos 
# del iterable son verdaderos (o si el iterable está vacío), y False en caso contrario.
lista = [1, 0, 3, 4]
resultado = all(lista)
print(resultado)  # Imprime: False (0 es considerado falso)

lista = [True, False, True]
resultado = all(lista)
print(resultado)  # Imprime: False

lista = [True, False, True]
resultado = all(lista)
print(resultado)  # Imprime: False

# la suma de todos los numeros
suma = sum(numero)
print(suma)