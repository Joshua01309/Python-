# Función simple
def animo():
    print('Animo que tus padres quieren ver a su hijo ser el mejor')
    
animo()

# Crear una función que tenga parametros
def datos(nombre, estudios):
    estudios = estudios.lower()
    if (estudios == 'ingeniero'):
        adjetivo = 'Titan'
    elif (estudios == 'medico'):
        adjetivo = 'Guerrero'
    else:
        adjetivo = 'pobre diablo'
        
    print(f'Sr {nombre} usted estudia como un {adjetivo}')
    
datos('josue', 'ingeniero')

# Contraseña aleatotria
def contraseña_random(num):
    letras ='abcfeghijklmnopqrstuwxyz'
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num*7
    c2 = num-1
    c3 = num+8
    contraseña = f'{letras[c1]}{letras[c2]}{letras[c3]}{num*3}'
    return contraseña, num # esto parece que returna los valores que le agregamos a la funcioon como una tupla
    
password, primer_num =contraseña_random() # aqui desempaquetamos
print(f'tu contraseña es {password}')
print(f'el numero que se utilizo fue {num}')



























