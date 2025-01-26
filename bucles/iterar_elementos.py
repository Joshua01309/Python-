helados = ['vainilla', 'chocolate', 'fresa']
for helado in helados:
    print(f'tu helado favorito es {helado}')
    
numeros = list(range(1,4))
for numero in numeros:
    resultado =  numero * 3
    print(resultado)
    
# para iterar o recorrer dos listas de manera sumultanea usamos zip tienen que ser del mismo tamaño
for helado, numero in zip(helados, numeros):
    print(f'recorriendo la lista helados {helado}')
    print(f'recoriendo la lista de numeros {numero}')
    
# forma no optima de recorrer una lista
numeros = list(range(1,4))
for numero in numeros:
    resultado =  numero * 3
    print(resultado)

# ESTO NO FUNCIONA EN CONJUNTOS
for num in range(len(numeros)):
    print(numeros[num])
    
# forma correcta de recorrer una lista con su indice
numeros = list(range(1,4))
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')


numeros = list(range(1, 4))
for indice, valor in enumerate(numeros):
    print(f'El índice es: {indice} y el valor es: {valor}')
    
# usando else
numeros = list(range(1,4))
for num in numeros:
    print(f'ejecutando el utlimo bucle, valor actual {num}')
else:
    print('el bucle termino')


#TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS, LISTAS Y CONJUNTOS