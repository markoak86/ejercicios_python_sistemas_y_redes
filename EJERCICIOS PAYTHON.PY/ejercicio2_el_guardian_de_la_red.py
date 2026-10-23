#SCRIPT DE AUTOMATIZACION
#1. Los datos maestros (Estructuras)
servidores_activos=[]
ssoo_permitidos={"Linux", "Windows", "Unix"}
datos_admin=("admin_root", "pass1234")

#2. Logica del calculo (Funciones)
def evaluar_seguridad(puerto):
    if puerto > 1024:
        return ("APLICACION")
    else:
        return ("SISTEMA")
    
#3. El registro (La funcion principal)

def registrar_equipo():
    nombre=str(input("introduce el nombre del equipo y pulse enter:"))
    ip=str(input("introduce la ip y pulse enter:"))
    puerto=int(input("intoduce le numero de puerto y pulse enter:"))
    sistema_operativo=str(input("introduce le sistema opertivo y pulse enter:"))
    nuevo_equipo= {"nombre": nombre, "ip": ip, "puerto": puerto, "sistema operativo": sistema_operativo}
    servidores_activos.append(nuevo_equipo)

    if sistema_operativo not in ssoo_permitidos:
        print("sistema operativo no oficial")

    print(evaluar_seguridad(puerto))

#4. El bucle de control (El menu interactivo)
while True:
    print("MENU\n1.REGISTRAR\n2.VER INVENTARIO\n3.SALIR")
    opcion=int(input("introduce una opcion y pulsa enter:"))
    if opcion==1:
        registrar_equipo()
    elif opcion==2:
        print(servidores_activos)
    elif opcion==3:
        break

