comidas =['pizza', 'hamburguesa', 'sushi', 'tacos', 'ensalada']

# voy a comer ciertos alimentos pero voy a evitar alguno de esta lista
for comida in comidas:
    if comida == 'sushi':
        continue
    print(f'me voy a comer una: {comida}')
    
# me duele la panza y si como suchi ya no puedo comer mas
for comida in comidas:
    if comida == 'sushi':
        break
    print(f'me voy a comer una: {comida}')
    
# agregando el else, si el break se ejecuta antes que else el codigo ya no ejecuta else
for comida in comidas:
    print(f'me voy a comer una: {comida}')
    if comida == 'sushi':
        break
else:
    print('terminado')
    
# recorrer una cadena de texto
mensaje = 'hola'
for letra in mensaje:
    print(letra)

# Definir la lista de números
numeros = [1, 2, 3, 4, 5]
numeros_multiplos = [x * 5 for x in numeros]
print(numeros_multiplos)  # Imprime: [5, 10, 15, 20, 25]