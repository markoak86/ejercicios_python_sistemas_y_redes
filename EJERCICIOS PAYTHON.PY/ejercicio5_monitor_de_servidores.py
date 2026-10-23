#CREAR UN PROGRAMA QUE GESTIONE UN GRUPO DE SERVIDORES

#1. Crear una clase que sirva de molde para cada servidor
class Servidor:
    def __init__(self, nombre, ip):
        self.nombre=nombre
        self.ip=ip
        self.estado= "offline"

    #crear un metodo que se impriman los servidores
    def __str__(self):
        return f"el servidor {self.nombre} con un ip {self.ip} esta {self.estado}"

    #crear otro metodo para encendre los servidores
    def encender_servidor(self):
        if self.estado=="offline":
            self.estado="online"

#2. Crear la logica para que una que recorra la lista de servidores y los monitorice
#primero creamos una lista vacia para añadir la lista de servidores
lista_servidores=[]

#despues creamos el bucle con el menu para añadir los nuevos servidores y para listalos
while True:
    print(f"MENU\n1.Introduce servidor\n2.Ver servidores\n3.Salir")
    opcion=int(input("introduce una opcion y pulsa enter:"))
    
    if opcion==1:
        nombre_srv=input("introduce el nobre del servidor y pulsa enter:")
        ip_srv=input("introduce la ip del servidor y pulsa enter:")
        
        #aqui creamos el objeto dentro de la clase servidor
        nuevo_srv= Servidor(nombre_srv, ip_srv)
        
        #y añadimos el servidor a la lista de servidores
        lista_servidores.append(nuevo_srv)
        print(f"el servidor {nombre_srv} se ha guardado con exito")

    elif opcion==2:
        for srv in lista_servidores:
            
            print(srv)


        

    elif opcion==3:
        break
    else:
        print("esa opcion no existe")

#por ultimo llamamos al metodo encender para encender los servidores y al metodo str para imprimir los servidores
for srv in lista_servidores:
    srv.encender_servidor()

for srv in lista_servidores:
    print(srv)

