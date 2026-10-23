#Crear un programa que gestione los servidores de un rak, cada servidor tiene unas caracteristicas propias y
# su estado y debe de persistir en un archivo cuando se cierre el programa.

#1.Crear un diccionario vacio para que haga el inventario y una clase como molde de casa servidor
inventario={}

class Servidor:
    def __init__(self, nombre, ip, rol, estado):
        self.nombre=nombre
        self.ip=ip
        self.rol=rol
        self.estado=estado
    
    def __str__(self):
        return f"El servidor {self.nombre}, con ip {self.ip}, cuyo rol es {self.rol} esta {self.estado}"
    
#2.Creamos una funcion con el menu para añadir añadir servidores, agregarlos al inventario y mostrarlos
while True:
    print("MENU DE REGISTRO DE SERVIDOR\n1.Añade servidor\n2.Mostrar el servidor\n3.Salir")
    opcion=int(input("introduce una opcion y pulsa enter:"))
    if opcion==1:
        nombre=input("introduce el nombre del servidor y pulsa enter:")
        ip=input("introduce la direccion ip y pulsa enter:")
        rol=input("introduce el rol y pulsa enter:")
        estado=input("introduce el estado del servidor y pulsa enter:")
        #añadir el servidor como nuevo objeto de la clase
        nuevo_servidor=Servidor(nombre, ip, rol, estado)
        #añadir el nuevo servidor al inventario
        inventario[nombre]=nuevo_servidor.__str__()
        #mostrar el servidor añadido con la funcion _srt_
        print(nuevo_servidor.__str__())
    elif opcion==2:
        print(inventario)
    elif opcion==3:
        break

# crear un archivo en el que se guarde el inventario
import io
archivo_inventario=open("inventario.txt", "a+")

#añadimos al archivo el inventario
escribir_inventario=archivo_inventario.write(str(inventario))

#y mostramos el contenido del archivo
leer_inventario=archivo_inventario.read(inventario)

#muy importante, cerramos el archivo
archivo_inventario.close()


