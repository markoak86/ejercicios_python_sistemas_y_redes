#CREAR UN PROGRAMA QUE GESTIONE LOS PUERTOS Y SERVIDORES:

#1. Crear un diccionario en el que la key sea el numero del puerto y el value el nombre del servidor
puertos_servidores={22: "SSH", 
                    80: "HTTP",
                    443: "HTTPS", 
                    3306: "MySQL"}

#2. Definar una funcion que pase la tupla de puertos y revise si el puerto esta activo o no.
def revisar_puertos(lista_de_puertos):
    for puerto in lista_de_puertos:
        if puerto in puertos_servidores.keys():
            print(f"el servidor {puerto}, esta ACTIVO")
        elif puerto not in puertos_servidores.keys():
            print(f"el servidor {puerto}, esta CERRADO")

lista_de_puertos=(22,25,80,5000)

#3. Llamar a la funcion.
revisar_puertos(lista_de_puertos)
