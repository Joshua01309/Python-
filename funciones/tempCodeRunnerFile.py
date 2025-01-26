numeros = [1,2,4,6,33]
filtro = filter(lambda numero: numero%2==0, numeros)
print(list(filtro))