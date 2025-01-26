# 1 Pedirle al usuario que diga cualquier texto real y: 
    # calcular cuanto tiempo tardaria en decir esa frase}
    # Cuantas palabras dijo?
    
# 2 Si se tarda mas de un minuto:
    # para flaco: tampoco te pedi un testamento?
    
# 3 Dalto habla un 30% mas rapido: 
    # Cuanto tardaria en decirlo?
    
frase = input('decirme una frase y te calculo cuanto tiempo tardarias en decirlas ')
palabras = frase.split(' ')
longitud = len(palabras)
print(f'dijiste {longitud} palabras y tardaste {longitud/2} segundos en decirlo')
print(f'Dalto lo diria en {longitud * 100 // 2 * 1.3 / 100} segundos en decirlo')
if longitud > 120:
    print('para man tampoco te pedi un testamento')