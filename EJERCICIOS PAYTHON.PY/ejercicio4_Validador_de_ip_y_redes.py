#CREAR UN SCRIPT PARA QUE GESTIONAR UNA LISTA DE IPS Y VERIFICAR SI PERTENECEN A LA RED LOCAL SON IPs EXTERNAS

#1- Datos:
#lista de ips que han intentado acceder al servidor
accesos=["192.168.1.15", "192.168.1.100", "10.0.0.5", "8.8.8.8", "192.168.1.20"]

#la red local empieza por:
prefijo_local="192.168.1"

#2- Funcion: funcion que reciba una ip que verifique si es una direccion local o externa
def clasificar_ip(ip):
    ip=input("introduce una ip y pulsa enter:")
    if ip.startswith(prefijo_local):
        return("LOCAL")
    else:
        return("EXTERNA")
    
#3- Diccionario: crear un diccionario para clasificar las ips locales y las ips externas
informe_de_red={"locales":[], "externas":[]}

#4- Bucle:crear un bucle for que vaya recorriendo los accesos y clasificarlos en locales y en externas
for ip in accesos:
    if ip.startswith(prefijo_local):
        informe_de_red["locales"].append(ip)
    else:
        informe_de_red["externas"].append(ip)

print(informe_de_red)

#5- llamar a la funcion para que te diga si una ip es local o externa
print(clasificar_ip(ip))

#SISTEMA DE GESTION DE USUARIOS DE UN SERVIDOR

#1-Crear una clase para definir cada objeto (cada usuario)
class Usuario:
    def __init__(self, nombre, rol, esta_adtivo):
        self.nombre=nombre
        self.rol=rol
        self.esta_adtivo=esta_adtivo
       
    def describir(self):
        return(f"el usuario {self.nombre}, con el rol {self.rol}, esta en situacion {self.esta_adtivo}")
    
#2-Datos. Crear una lista con barios objetos de la clase (cada objeto es un usuario)
db_usuarios=[Usuario("Ana", "admin", True),
             Usuario("Pedro", "user", False),
             Usuario("Marta", "user", True)]


#3-Bucle, que clasifique los usuarios si estan adtivos o estan bloqueados
for usu in db_usuarios:
    resumen={"adtivos":1, "boqueados":1}
    if usu.esta_adtivo== True:
        resumen["adtivos"] += 1
    elif usu.esta_adtivo== False:
        resumen["boqueados"] += 1

    print(usu.describir())

print(resumen)

#MONITOR DE SERVICIOS DE RED. CADA SERVIDOR TIENE UNA LISTA DE SERVICIOS Y CUALES ESTAN SATURADOS Y CUALES NO

#1- Clase Servidor. Crear una clase con cada servidor con dos metodos
class Servidor:
    def __init__(self, nombre, ip, servicios):
        self.nombre= nombre
        self.ip= ip
        self.servicios= servicios
        
    def ver_info(self):
        return(f"el servidor llamado {self.nombre}, tiene una ip {self.ip}")
    
    def contar_servicios(self):
        return(len(self.servicios))
    
#2- El inventario. Crear un dicionario que contenga los objetos de la clase(servidores) y organizarlos por su funcion.
infraestructura={"web":Servidor("Web-prod", "192.168.1.10", ["http", "https", "ssh"]),
                 "db":Servidor("DB-master", "192.168.1.20", ["mysql","ssh"]),
                 "proxy":Servidor("Nginx-LB", "192.168.1.30", ["http", "https", "ssh", "snmp", "ntp"])}

#3- Crear un bucle para que se impriman los los servidores y si los servidores tienen mas de tres servicios imprimir una alerta
for srv in infraestructura.values():
    print(srv.ver_info())
    if srv.contar_servicios() > 3:
        print(f"ALERTA: el servidor {srv.ver_info()}, esta sobrecargado")
    else:
        print(f"El servidor {srv.ver_info()} esta en estado normal")

#4-Crear una funcion que recorrar los servidores y y que te diga a que nombre de servidor pertenece una ip
def buscar_ip():
    ip=input("introduce una ip y pulsa enter:")
    for srv in infraestructura.values():
        if ip==srv.ip:
            print(f"la ip {ip}, corresponde al servidor {srv.nombre}")

print(buscar_ip())       
    
