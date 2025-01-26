multiplo = lambda x: x*2
print(multiplo(7))

# creando una funcion que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
numeros = [1,2]
# utilizando la funcion filter
filtro = filter(es_par, numeros)

print(list(filtro))

# utilizando labda
numeros = [1,2,4,6,33]
filtro = filter(lambda numero: numero%2==0, numeros)
print(list(filtro))