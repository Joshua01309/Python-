import paquete
print(type(paquete))

# junto con el paquete que se en la carpeta paquete y el archivo que avala que es un paquete
# '__init__.py lo que hace es que es un tipo de enrutamiento

# del paquete accedemos a la funcion
    # siempre se le da prioridad a la carpeta
import paquete.saludar
print(paquete.saludar.saludar('josefina'))

# para acceder a un paquete de un paquete que es un subpaquete
    # ambos tendrian que tener el archivo enrutado de '__init__.py
    # import.paquete.subcarpeta.saludar
    