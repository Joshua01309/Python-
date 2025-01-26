# Las variables almacenarán los datos que se necesiten en el programa.
# Las variables se pueden declarar de la siguiente manera:
# nombre_de_la_variable = valor_de_la_variable 
# Declaramos la variable nombre y le definimos el valor "Josue"
# Ejemplo:
nombre = "Josue"
# las variables se pueden reasignar
nombre = "Josue ivan"
nombre = "Josue ivan gonzalez"
print(nombre)

numero = 123
numero = 124
numero += 1
print(numero)

# concatenar variables
nombre = "Josue"
print("Hola " + nombre)
# la concatenaciobn sirve para unir variables de tipo string
# podemos utilizar la concatenacion de tipo f-string
print(f'Hola {nombre}')
# Otro ejemplo
nombre = "Josue"
mensaje = f'bienvenido {nombre}'
print(mensaje)

nombre = "Josue"
mensaje = f'bienvenido {nombre}'
del nombre
print(mensaje)

# El resultado de ejecutar este código será la impresión de la cadena "bienvenido Josue".
# La eliminación de la variable nombre no afecta a la variable mensaje
# porque mensaje ya contiene el valor 
# formateado antes de que nombre sea eliminada.
nombre = "Josue"
del nombre
mensaje = f'bienvenido {nombre}'
print(mensaje)

# ahora con boleanos, operadores de pertenencia
nombre = 'Josue'
mensaje = f'bienvenido {nombre.lower()}'
print('josue' in mensaje)
    # Hay que tener en cuenta que la comparación es case sensitive,

print('ivan'not in mensaje)

#Camel case: case es una convención de nomenclatura 
# en la que las palabras se concatenan sin espacios y 
# cada palabra, excepto la primera, comienza con una letra mayúscula. 
# Esta convención se utiliza comúnmente en la programación para nombrar variables y funciones.

#Ejemplos de camel case:
#miVariable
#nombreCompleto
#calcularAreaCirculo

#Snake case es una convención de nomenclatura en la que las palabras se separan por
# guiones bajos (_) y todas las letras están en minúsculas. Esta convención se 
# utiliza comúnmente en la programación para nombrar variables y funciones, 
# especialmente en lenguajes como Python.

#Ejemplos de snake case:

#mi_variable
#nombre_completo
#calcular_area_circulo
































string = "hola mundo"
print(string)

string = 'hola mundo'
string = 'hola mundo\'s'
string = "hola mundo \"s"
print(string)

string = 'hola mundo'[5:10]
print(string)

# string y sliding
string = 'Helado de vainilla'
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print(string.replace('vainilla', 'chocolate'))
print(string.split(' '))
print(string.strip())
print(string.lstrip())
print(string.split())
print(string.join(''))
print(string.find('vainilla'))
print(string.count('a'))

#numero de caracteres
nombre = input('nombre').lower()
print(len(nombre))
# pide al usuario su nombre y apellido, concatena e imprime el resultado y tambien imprime
# el numero de caracteres
nombre = input('nombre').lower()
apellido = input('apellido').lower()
sumatoria = len(nombre) + len(apellido)
print(f'tu nombre es {nombre} y tu apellido {apellido} y tienen el numero de caracteres {sumatoria}')

#Pide al usuario su primer nombre, si el número de caracteres es menor a 5, pide su apellido, concatena, 
# pasa todo a mayúsculas e imprime, de lo contrario imprime todo en minúsculas
nombre = input('dame tu nombre ')
nombre_len = len(nombre)
apellido = input('dame tu apellido ')
if nombre_len < 5:
    print(f'tu nombre es {nombre.upper()} y tu apellido es {apellido.upper()} ')
else:
    print(f'tu nombre es {nombre.lower()} y tu apellido es {apellido.lower()}')


# modulos
import math  # Importa el módulo math

hola = math.sqrt(4)  # Calcula la raíz cuadrada de 4
print(hola)  # Imprime: 2.0

# Crea un programa que pida un número al usuario y lo multiplique por dos.

import math  # Importa el módulo math
num = int(input('dame un numero '))
num_2 = num * 2
print(f'Tu numero multiplicado por 2 es {num_2}')


import math  # Importa el módulo math

# Pide al usuario un número, calcula su raíz cuadrada y muestra el resultado redondeado a 2 decimales
num = int(input('dame un numero '))
raiz_cuadrada = math.sqrt(num)
raiz_cuadrada_redondeada = round(raiz_cuadrada, 2)
print(f'La raíz cuadrada de tu número, redondeada a 2 decimales, es {raiz_cuadrada_redondeada}')

# Muestra el valor de pi, usando math, y mostrarlo con 5 decimales.
valor_pi = round(math.pi, 5)
print(f'El valor de pi con 5 decimales es {valor_pi}')

#Crea un programa que pida al usuario el radio de un círculo y luego devuelva su área.
radio = float(input('Dame el radio de un círculo: '))
area = math.pi * (radio ** 2)
print(f'El área del círculo con radio {radio} es {area}')

# Pide al usuario la altura y radio de un cilindro y devuelve su volumen.
altura = float(input('Dame la altura del cilindro: '))
radio = float(input('Dame el radio del cilindro: '))
volumen = math.pi * (radio ** 2) * altura
print(f'El volumen del cilindro con altura {altura} y radio {radio} es {volumen}')
