#1 Diferencia en porcentaje entre el curso actual y:
    # a) el mas rapido de otros cursos
    # b) el mas lento de otros cursos
    # c) el promedio de otros cursos
    
#2  Porcentaje de material inservible que se reduce en:
    # el promedio de los cursos
    # el curso actual (este curso)
    
#3  Ver 10 horas de este curso a cuantas de otros curso equivale

# 1
# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Diferencias de duración
diferencia_min = 100 - dalto_curso/otros_cursos_min * 100
diferencia_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - dalto_curso/otros_cursos_promedio * 100

print(f'El curso de dalto dura {diferencia_min}% menos que el curso mas rapido')
print(f'El curso de dalto dura {diferencia_max}% menos que el curso mas lento')
print(f'El curso de dalto dura {diferencia_promedio}% menos que cursos en promedio')

# 2
# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Calculando del porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 //crudo_dalto / 10

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'El curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio0')

# 3
# Diferencias si los cursos duran 10 hrs
print(f'Ver 10hrs de este curso equivalen a ver {otros_cursos_promedio *100 // dalto_curso / 10 } hrs de otros cursos')
print(f'Ver 10hrs de otros cursos equivalen a ver {dalto_curso * 100 // otros_cursos_promedio /10} hrs de este curso')

