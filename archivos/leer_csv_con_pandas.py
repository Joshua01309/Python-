import pandas as pd
# print(type(pd))
df = pd.read_csv('archivos\\datos.csv')
df2 = pd.read_csv("archivos\\datos.csv")
#, names = ['name', 'lastname', 'age'])

print("Columnas del DataFrame:", df.columns)
# opteniendo los datos de la columna nombre
nombres = df['nombre']

# data frame son estructuras de datos bidimensionales similares a una hoja de calculo 

# ordernar por edad
df_ordenado = df.sort_values('edad')
print(df_ordenado)

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 2 filas con head()
primeras_filas = df.head(2)

#accediendo a las últimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape
#filas_y_columnas_totales = df.shape
# filas_totales = df.shape[0]
# columnas_totales = df.shape[1]


#obteniendo data estadística del dataframe:
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)





#slidesing: es una tecnica que nos permite identificar el principio y el final en la forma en que accedemos a los elementos
# string = '0123456789'
# print(string[:])