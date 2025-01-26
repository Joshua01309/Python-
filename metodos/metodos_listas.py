# Crear una lista con la funcion list
make = list(['hola', 'SoyGerman', True])
print(make)

# funcion len(): devuelve la cantidad de elementos
cadena = 'josue'
longitud_cadena = len(cadena)
print(longitud_cadena)  # Imprime: 5

lista = ['hola', 'SoyGerman', True]
longitud_lista = len(lista)
print(longitud_lista)  # Imprime: 3

# append: agrega un nuevo elemento a una lista en especifico al final
lista.append('25')
print(lista)

# Agregando un nuevo elemento a la lista en un indice especifico
lista.insert(2, 'insertado')
print(lista)

# pasar una lista a otra lista o agrega varios elementos a una lista
lista.extend(['ext', 'tend'])
print(lista)

# Eliminar un elemento de la lista
print(len(lista))
lista.pop(3)
print(len(lista))
# si queremos eliminar el ultimo elemento de la lista es -1
lista.pop(-1)
print(lista)

# Removiendo un elemento de la lista por su valor
lista.remove('insertado')
print(lista)

#Eliminando todos los elementos de una lista
# lista.clear()

# la funcion sort() funciona para ordenar los elementos de manera ascendente
# si usamos el parametro reverse=True lo ordena en reversa
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#invirtiendo los elementos de una lista
lista.reverse()
print(lista)

# en las tuplas algunas de sus funciones nos facilita encontar elementos (index) que contiene puesto
# que estas no se pueden modificar o alterar
print(dir((4,5)))