# En Python, set es una colección desordenada de elementos únicos. Los conjuntos (sets) 
# se utilizan para almacenar múltiples elementos en una sola variable, pero a diferencia 
# de las listas o tuplas, no permiten elementos duplicados. Los conjuntos son útiles 
# para realizar operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

# En conjunto set solo podemos colocar datos que no son mutables
conjunto = set(['josue', 'ingeniero', 20])
print(conjunto)
# si queremos colocar una lista o un dicccionario, dentro de este conjunto nos lanzara un error 
#conjunto = set(['josue', 'ingeniero', 20, ['dato1', 'dato2']])
#  tampoco otro conjunto,
#   conjunto1 = {'dato1', 'dato2'}
#   conjunto2 = {conjunto1, 'dato3'}
# pero si podemos colocar una tupla
conjunto = set(['josue', 'ingeniero', 20, ('dato1', 'dato2')])
print(conjunto)

# para meter un cojunto dentro de otro conjunto metemos la funcion frosenset
conjunto = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto, 'dato3'}
print(conjunto2)

# Teoria de conjuntos
# depende de la perspectiva o posicion

#verificar si es un subcojunto
conjunto1 = {1,2,3}
conjunto2 = {1,2,3,4,5}

resultado = conjunto1.issubset(conjunto2)
resultado = conjunto1 <= conjunto2
print(resultado)

# verificando si es un superconjunto

resultado = conjunto1.issuperset(conjunto2)
resultaod = conjunto1 > conjunto2
print(resultado)

# verificar si hay un numero en comun, es falso cuando almenos tienen un elemento en comun
resultado = conjunto1.isdisjoint(conjunto2)
print(resultado)