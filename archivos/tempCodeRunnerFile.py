import pandas as pd
# print(type(pd))
df = pd.read_csv('archivos\\datos.csv')
#, names = ['name', 'lastname', 'age'])

print("Columnas del DataFrame:", df.columns)
# opteniendo los datos de la columna nombre
nombres = df['nombre']