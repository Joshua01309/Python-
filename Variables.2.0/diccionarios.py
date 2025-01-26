# Creando un diccionario con la funcion dic
diccionario = dict(nombre = 'josue', carrera = 'finanzas')
print(diccionario)

#las listas no pueden ser claves pero si las tuplas, se puede meter frosenset para meter cojunto
diccionario = {('hola', 'german'): 'tupla'}
diccionario = {frozenset(['hola', 'german']): 'frosenset'}
print(diccionario)

# creando diccionarios con fromkey valor por defecto none
diccionario = dict.fromkeys(['nombre', 'apellido'])
print(diccionario)

# Creando diccionarios fromkeys con dos parametros
# Creando diccionarios fromkeys con dos parametros y valor por defecto 'sabe'
diccionario = dict.fromkeys(['nombre', 'apellido'], 'sabe')
print(diccionario)