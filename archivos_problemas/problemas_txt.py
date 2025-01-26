# 2 listas, nombres y apellidos
nombres = ["Juan", "Maria", "Pedro", "Luis", "Ana"]
apellidos = ["Perez", "Gomez", "Lopez", "Martinez", "Garcia"]

# registrar información en un txt 
with open('archivos_problemas_resueltos\\nombres_apellidos.txt','w') as arch:
    arch.writelines('Los datos son:\n\n')
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n-----\n') for n,a in zip(nombres,apellidos)]