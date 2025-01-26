import pandas as pd
df = pd.read_csv('archivos_problemas_resueltos\\datos1.csv')
#   print(df.columns)

# cambiar el tipo de dato de una columna
# convertir a str los datos de una columna
df['age']= df['age'].astype(str)
# mostrar el primer elemento de la columna edad
#   print(type(df['age'][0]))

#replanzando datos
df['apellidos'].replace('dalto', 'crack', inplace = True)
#print(df['nombre'])

# eliminando filas con datos vacios
df = df.dropna(how='any', axis=0, inplace=False)

# eliminar filas repetidas
df = df.drop_duplicates()


# Creando un CSV con el dataframe resultante (limpio)
df.to_csv('archivos_problemas_resueltos\\datos1_limpios.csv') 
