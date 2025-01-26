# Lista
cosas_en_mi_cochera = ['lavadora', 'escoba', True, 18]
# una lista contiene un conjunto de valores o elementos, los cuales podemos acceder a ellos
#por medio de los indices el elemento 1 se contiene en el indice 0
print(cosas_en_mi_cochera[0])

# Las listas se pueden modificar 
cosas_en_mi_cochera[0] = 'microondas'
print(cosas_en_mi_cochera[0])

# si defino una tupla con parentesis diferente a lo de una lista con corchetes
# esta lista ya no la podre modificar si lo intente hacer me arrojara un error
cosas_en_mi_cochera = ('lavadora', 'escoba', True, 18)
#  print(cosas_en_mi_cochera[0])
# no podemos modificarlos individualemnte los elementos de una tupla pero si podemos reasignar toda la tupla de nuevo
cosas_en_mi_cochera = ('lavadora', 'escoba', True, 18)
print(cosas_en_mi_cochera)
cosas_en_mi_cochera = ('microondas', 'trapeador', False, 8)
print(cosas_en_mi_cochera)

# Un conjunto sirve de igual manera que una lista con la diferencia que 
# los elementos repetidos solo los imprime una vez, no podemos modificarlos 
# individualemnte y los elementos estan contenidos en {} llaves
# Contiene datos de manera desordenada

conjunto = {'vainilla', 'vainilla', 'chocolate', 'fresa'}
print(conjunto)

# Diccionario
# Un diccionario contiene pares de clave:valor, los cuales podemos acceder por medio de la clave
favorite_lenguages = {'mariana': 'python', 'ivan': 'java', 'ana': 'c++'}
print(favorite_lenguages['mariana'])

# Podemos agregar nuevos pares clave:valor al diccionario
favorite_lenguages['juan'] = 'javascript'
print(favorite_lenguages)

# También podemos modificar los valores asociados a una clave existente
favorite_lenguages['ivan'] = 'go'
print(favorite_lenguages)

# Podemos eliminar un par clave:valor usando la clave
del favorite_lenguages['ana']
print(favorite_lenguages)