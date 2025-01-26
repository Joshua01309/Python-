# un alumno es profesor
# un alumno es asistente
    # 1 pedir la edad de los estudiantes y ordenarla de menor a mayor
    # el mayor es el profesor y el menor el asistente
    

def lista_compañeros(cantidad):
    alumnos = []
    for i in range(cantidad):
        name = input('Cual es tu nombre ')
        edad = int(input('Dame tu edad '))
        compañero = (name, edad)
        alumnos.append((compañero))
    alumnos.sort(key = lambda x:x[1])
    asistente = alumnos[0][0]
    profesor = alumnos[-1][0]
    return asistente, profesor
asistente, profesor = lista_compañeros(3)  
print(f'El asistente es: {asistente} y el profesor es: {profesor}')
        
