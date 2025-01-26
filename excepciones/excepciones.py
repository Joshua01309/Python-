def sumar():
    while True:
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        try: 
            resultado = int(a) + int(b)
            break
        except ValueError:
            print('apagalo oto')
    return resultado

print(sumar())