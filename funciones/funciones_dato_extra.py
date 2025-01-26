def datos(nombre,profesion,adjetivo):
    return f'Hola {nombre} estudiaste {profesion} sos un {adjetivo}'

# cambiando el orden
def datos(nombre,profesion,adjetivo):
    return f'Hola {nombre} estudiaste {profesion} sos un {adjetivo}'

resultado = datos(profesion = 'ingenieria', nombre = 'Josue', adjetivo='crak')
print(resultado)

# colocando un argumento por defecto
def datos(nombre,profesion,adjetivo= 'boludo'):
    return f'Hola {nombre} estudiaste {profesion} sos un {adjetivo}'

resultado = datos(profesion = 'ingenieria', nombre = 'Josue')
print(resultado)