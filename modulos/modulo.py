#importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludo_raro = saludar_como_coscu("Fran")

#mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)















# import modulo_saludar as m_s      podemos llamar al modulo de una manera mas corta
# from modulo_saludar import saludo, saludo_comico as s_c # direcatamente llama a la funcion

# 'from funciones_buenas.modulo_saludar import saludo, saludo_comico as s_c'
# cuando creamos otra carpeta en donde creamos las definiciones para llamarla tenenos que 
# hacerlo de esta manera

# saludos = saludo('josue')
# print(saludos)
# saludito = s_c('josefa')
# print(saludito)

# print(type(modulo_saludar))

# import modulo_saludar as m_s
# print(dir(m_s))

# accedemos al nombre de este modulo
# print(__name__)
# accedemos al nombre del modulo llamado
# print(m_s. __name__)
