def es_primo(num):
    for i in range(2, num-1):
        if num%i==0: return False
    return True

def primo_hasta(num):
    lista = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True: lista.append(i)
    return lista

resultado = primo_hasta(15)
print(resultado)