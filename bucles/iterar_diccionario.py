# para iterar un diccionario e imprimir su llave o clave es exactamente igual que listas
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

for llave in mi_diccionario:
    print(llave)
    
# para iterar tanto la llave y el valor utilizamos la funcion items
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
for datos in mi_diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la llave es: {key} y el valor es: {value}')
