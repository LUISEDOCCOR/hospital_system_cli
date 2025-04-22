#importar librerias
import json, uuid, os

class Basededatos:
    #Pedir como parámetro el nombre del archvio donde se guardaran los datos
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        #Declarar variable con la ruta donde se guardara mi archvio
        #La ruta es de mi carpeta actual, en la carpeta "datos", en el arhcivo con nombre (nombre pasado como argumento).json
        self.archivo = f"./datos/{self.nombre_archivo}.json"
        #Si no esta la carpeta datos la creamos
        if not os.path.exists("./datos"):
            os.makedirs("./datos")
        #Si no esta el archivo (ruta), lo creamos, y escrivimos en el una lista vacía
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as archivo:
                json.dump([], archivo)

    #EL método empieza con __ porque es privado, es decir no se puede usar en una instancia
    #https://www.codigofacilito.com/articulos/atributos-privados-python
    def __leer_archivo(self):
        with open(self.archivo, "r") as archivo:
            return json.load(archivo)

    def __escribir_archivo(self, contenido):
        with open(self.archivo, "w") as archivo:
            json.dump(contenido, archivo, indent=4)

    def crear(self, datos: dict):
        #Intenta
        try:
            #A los datos le agregamos un id con un el valor de una serie de números únicos
            datos["id"] = str(uuid.uuid4())
            contenido = self.__leer_archivo()
            #Al contenido se le agregan los nuevos datos
            contenido.append(datos)
            #El contenido con los nuevos datos, se escribe en el archivo
            self.__escribir_archivo(contenido)
            return True
        #Si falla retornamos  un false
        except:
            return False

    def editar(self, id: str, datos: dict):
        try:
            contenido = self.__leer_archivo()
            #Reccorremos cada elemnto del contenido
            for elemento in contenido:
                #Si el id de un elemnto coincide con el que estamos buscando actulizamos sus datos, con los nuevos
                if elemento["id"] == id:
                    elemento.update(datos)
                    #Terminamos el for
                    break
            #Escribimos el archivo con el nuevo contenido
            self.__escribir_archivo(contenido)
        except:
            return False

    def eliminar(self, id: str):
        try:
            contenido = self.__leer_archivo()
            #EL nuevo contenido son todos los elemntos, menos el que tenga el mismo id que se paso de parametro
            nuevo_contenido = [elemento for elemento in contenido if elemento["id"] != id]
            self.__escribir_archivo(nuevo_contenido)
            return True
        except:
            return False

    def obtener_por_id(self, id: str):
        try:
            contenido = self.__leer_archivo()
            for elemento in contenido:
                #retornamos el elemnto que tenga el mismo id que se paso como parametro
                if elemento["id"] == id:
                    return elemento
        except:
            return False

    def obtener_todos(self):
        return self.__leer_archivo()
