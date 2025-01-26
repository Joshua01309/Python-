# Definición de un diccionario en Python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

print(mi_diccionario)

# Obtener las llaves del diccionario
llaves = mi_diccionario.keys()

# Imprimir las llaves del diccionario
print(llaves)
# Obtener el valor de una llave específica usando el método get
valor_nombre = mi_diccionario.get("nombre")
valor_edad = mi_diccionario.get("edad")

# Imprimir los valores obtenidos
print("Nombre:", valor_nombre)
print("Edad:", valor_edad)

# Obtener los pares clave-valor del diccionario
items = mi_diccionario.items()

# Imprimir los pares clave-valor
print(items)

mi_diccionario.pop("nombre")  # Elimina la clave "nombre" y su valor
# mi_diccionario.clear()  # Elimina todos los elementos del diccionario