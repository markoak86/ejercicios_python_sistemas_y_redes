#CREAR UN SCRIPT PARA PROCESAR UNA LISTA DE SERVIDORES, QUE FILTRE LOS QUE ESTAN ACTIVOS Y CATEGORIZARLOS POR SISTEMA OPERATIVO.

#1- DATOS INICIALES.
servidores=[("SRV-WEB", "192.168.1.10", "online", "linux"),
            ("SRV-BD", "192.168.1.20", "offline", "linux"),
            ("SRV-WIN", "192.1168.1.30", "online", "windows"),
            ("SRV-BACKUP", "192.168.1.40", "online", "linux"),
            ("SRV-DEV", "192.168.1.50", "offline", "windows")]

ssoo_permitidos={"linux", "windows", "macOS"}

#2- CREAR UN BUCLE PARA QUE LOS QUE ESTEN ONLINE SE AÑADAN A UNA NUEVA LISTA DE SERVIDORES ADTIVOS.
srv_adtivos=[]
for srv in servidores:
    if srv[2]=="online":
        srv_adtivos.append(srv)

print(srv_adtivos)

#3- CREAR UN DICCIONARIO PARA CONTAR LOS SERVIDORES PARA CADA SISTEMA OPERATIVO.
conteo_ssoo={"linux":0, "windows":0,"macOS":0}
for srv in servidores:
    if srv[3].lower()=="linux":
        conteo_ssoo["linux"] +=1
    elif srv[3].lower()=="windows":
        conteo_ssoo["windows"] +=1
    elif srv[3].lower()=="macOS":
        conteo_ssoo["macOS"] +=1
   
print(conteo_ssoo)

#4- CREAR UB BUCLE PARA DETERMINAR SI EL SO DEL SERVIDOR PERTENECE A LOS SSOO PERMITIDOS
for srv in servidores:
    if srv[3] in ssoo_permitidos:
        print(f"el servidor {srv[0]}, es un servidor permitido")
    else:
        print(f"ALERTA: el servidor {srv[0]}, es un servidor no permitido")
        






    



