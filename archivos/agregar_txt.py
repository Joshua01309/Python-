with open('archivos\\texto_josue.txt','a',encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregando lineas
        archivo.write(f"Linea {i+1} agregada\n")
#a lo que hace es agregar texto