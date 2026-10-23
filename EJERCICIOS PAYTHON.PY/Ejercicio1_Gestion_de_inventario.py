#en un DD.CC. crear un programa para gestionar los equipos.
empresa="centro de datos.com"
numero_de_servidores=3
servidores=["Web-01", "DB-01", "Buckup-01"]
ips=("192.168.3.1", "192.168.10.3", "192.168.5.6")
sistemas_operativos_instalados={"Ubuntu", "Debian", "Windows"}
servidor_principal={ 1:["Web","01","192.168.3.1","Ubuntu"],  2:["DB", "01", "192.168.10.3", "Debian"], 3: ["Buckup", "01", "162.168.3.1", "Windows"]}

#recorrer todos los sevidores y si el servidor encontrado es DB-01 imprimir servidor critico
for srv in servidores:
    if srv=="DB-01":
        print (f"el servidor {srv} es un servidor critico")
    else:
        print (f"el servidor {srv} es un servidor estandar")
espacio_servidor=500
espacio_usado_servidor=240
porcentaje_servidor_usado=(espacio_usado_servidor/espacio_servidor)*100
print(porcentaje_servidor_usado)

#ahora vamos a hacer que el programa interaccione con el usuario
nuevo_servidor=input(str("introduce un nuevo servidor:"))
servidores.append(nuevo_servidor)#añadimos el nuevo servidor al la lista "servidores"
print(servidores)

if porcentaje_servidor_usado >=80:
    print("ALERTA: Servidor sobrecargado")
elif porcentaje_servidor_usado >50:
    print("ESTADO NORMAL DEL SERVIDOR")
else:
    print("AVISO:Carga moderada")

for servidor in servidor_principal.values():
    print(f"el servidor: {servidor[0]} con ip: {servidor[2]} y sistema operativo {servidor[3]}")

nuevo_so=input(str("introduce un sistema operativo:"))
sistemas_operativos_instalados.add(nuevo_so)
print(sistemas_operativos_instalados)

#crear una funcion para calcular el estado del disco
def verificar_disco(espacio_disco, espacio_usado_disco):
    porcentaje = (espacio_usado_disco/espacio_disco)* 100
    return porcentaje

print(verificar_disco(400,100))
resultado_disco= verificar_disco(400,100)

#y otra funcion para lanzar alertas segun el estado del disco
def lanzar_alerta(resultado_disco):
    if resultado_disco >= 80:
        return("estado de disco critico")
    elif resultado_disco > 50:
        return("estado de disco moderado")
    else:
        return("estado del disco normal")

print(lanzar_alerta(resultado_disco))

#crear una funcion para que podamos añadir servidores a un inventario
nuevo_inventario=[]
def añadir_servidor():
    nombre=input(str("intoduce el nombre del servidor y pulsa enter:"))
    id=input(str("introduce la id del servidor y pulsa enter:"))
    ip=input(str("introduce la ip y pulsa enter:"))
    sistema_operativo=input(str("introduce el sistema operativo y pulsa enter:"))
    nuevo_srv={"nombre":nombre, "id":id, "ip":ip, "sistema operativo":sistema_operativo}
    nuevo_inventario.append(nuevo_srv)

añadir_servidor()
print(nuevo_inventario)