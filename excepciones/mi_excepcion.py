#creando mi propia excepción personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        

#Lanzando mi propia excepcion
#raise MiExcepcion("alguien necesita regresar a primaria")

#manejandola
try:
    raise MiExcepcion("vuelvete a primaria boludo")
except:
    print("Como vas a cometer ese error?")