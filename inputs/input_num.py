# si colocamos una cadena o un string a una operacion aritmetica
# lo que optendremos es ese mismo caracter cierto numero de veces

multiplo = num*3
print(multiplo)

# para solucionar esto lo que podemos hacer es colocar
# int que transforma la entrada en un numero
num = input('Dame un numero ')
multiplo = int(num)*3
print(multiplo)

# para decimales utilizamos la funcion float lo cual nos regresa un numero con decimal
num = input('Dame un numero con decimal o de base 10 ')
multiplo_flot = float(num)*3
print(multiplo_flot)