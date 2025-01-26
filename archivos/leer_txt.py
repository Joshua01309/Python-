# usando open para abrir un archivo
archivo = open('archivos\\texto_josue.txt', encoding='UTF-8')

# leer archivo completo
#archivo = archivo.read()
#       print(archivo)
# establecer codificacion universal que lee todos los caracteres

# para leer una linea especifica/ si no lee la linea completa le la cantidad de caracteres
# la funcion readline tiene el problema que si el archivo es muy grande se puede consumir toda la
# memoria ram
#   linea_1 = archivo_sin_leer.readline()

# una vez que el archivo se lee por motivos de seguridad te arroja un caracter vacio, tenemos que cerrar el archivo
lineas = archivo.readlines()
    
# cerrar el archivo

archivo.close()

print(lineas)