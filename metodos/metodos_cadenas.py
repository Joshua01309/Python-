# dir es una funcion
cadena = "example string"
print(dir(cadena))
print(dir(5))

# metodos
# todo mayusculas
metodos = cadena.upper
# minusculas
metodos = cadena.lower
# funciona como titulo
metodos = cadena.capitalize

# find encuentra la primera concidencia del caracter en una cadena, devuelve -1 si no hay concidencias
metodos = cadena.find('x')
print(metodos)
# index funciona de manera similar a find pero esta lanza una exepcion
metodos = cadena.index('x')

# si es numerico es TRUE si no FALSE
metodos = cadena.isnumeric()
print(metodos)
numeros = '4444445'
print(numeros.isnumeric())
# alfanumerico: no reconoce caracteres especiales como el espacio
alfa = 'HolaSoyGerman'
print(alfa.isalpha())

# contar: sirve para contar las coincidencias de una cadena dentro de otra cadena
print(cadena.count('s'))  
# la funcion len sirve para saver cuantos caracteres tiene una cadena
fnc_len = 'hola'
print(len(fnc_len))

# Para verificar si una cadena empieza con otra cadena
empieza = 'Empiezo yo'
print(empieza.startswith('E'))
# si termina}
print(empieza.endswith('o'))
# remplazar una parte de la cadena por otra
print(empieza.replace('Empiezo', 'primero'))

# convertir cadenas a listas
string = 'Como,estamos,parcero'
list_string = string.split(',')
print(list_string)
