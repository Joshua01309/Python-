#si el modulo estuviera dentro de una carpeta en la misma ruta 
# import funciones_buenas.saludar as m_saludar
#   print(m_saludar.saludar.saludar('josue'))

import sys
# nombre de los modulos
    #print(sys.builtin_module_names)

sys.path.append("c:\\Users\\ivanj\\OneDrive\\Escritorio\\Python\\funciones_buenas")

import saludar as modulo_saludo

print(modulo_saludo.saludar("josue"))

















# si el modulo estuviera en una misma ruta 'import funciones_buenas.saludar'
# print(funciones_buenas.saludar('josue'))

# import sys
# sys.path.append('c:\\Users\\ivanj\\OneDrive\\Escritorio\\Python\\funciones_buenas')
# print(sys.path)

# import saludar as modulo_saludo
# print(modulo_saludo.saludar('josue'))

