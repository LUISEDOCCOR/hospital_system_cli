# Del archivo basededatos.py importamos la clase Basededatos
from basededatos import Basededatos
#Importamos esta libreia que nos ayudara a convertir un texto de una sola linea en varias
from textwrap import fill

class Persona:
    #Creamos una instancia de la clase basededatos y la llamamos bd
    bd = Basededatos("persona")
    #A la hora de crear una instancia de esta clase pediremos como parametro los siguiente:
    def __init__(self, nombre, edad, correo, celular, genero, tipo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.celular = celular
        self.genero = genero
        self.tipo = tipo

    #Definimos un método que retorne la estrucutra que deben de llevar los datos, este método es de instancia
    def construir_datos(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "correo": self.correo,
            "celular": self.celular,
            "genero": self.genero,
            "tipo": self.tipo # Para poder identificar a las personas, agregamos esta propiedad,
            # que en este caso podría ser "Paciente" o "Doctor".
        }

    # Estos son métodos de clase, lo que significa que no se tiene que hacer una instancia para usarlos.
    # Se usan de esta manera: Persona.método()
    # si fuera un método de instancia, se usaría así:
    # x = Persona(atributos...)
    # x.método()
    # Al definir métodos de clase, se usa @classmethod,
    # y en lugar de pasar como parámetro "self", se pasa "cls"

    @classmethod
    def editar(cls, id: str, datos: dict):
        #accedemos a la instancia db a traves de cls ya que es una propiedad nivel clase
        return cls.bd.editar(id, datos)

    @classmethod
    def eliminar(cls, id: str):
        return cls.bd.eliminar(id)

    @classmethod
    def obtener_por_id(cls, id: str):
        return cls.bd.obtener_por_id(id)

    @classmethod
    def obtener_todos(cls, tipo: str):
        #retornamos los elemntos cuya clave "tipo" coincida con el valor pasado como parámetro
        return cls.bd.obtener_por_clave_valor("tipo", tipo)

#Creamos la clase Doctor, que es una herencia de la clase Persona
#esto significa que conserva todos los atributos y métodos de las clase padre (Persona)
class Doctor(Persona):
    def __init__(self, nombre, edad, correo, celular, genero, especialidad):
        super().__init__(nombre, edad, correo, celular, genero, tipo="doctor")
        #Como parámetro nuevo pedimos una especialidad
        self.especialidad = especialidad

    #Sobrescribimos el método obtener_todos, retornando lo mismo que hace el original, con la diferencia 
    #que el tipo lo ponemos en default como doctor
    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("doctor")

    def crear (self):
        #Usamos el método construir datos, que retorna un diccionario con la estructura de los datos
        datos = self.construir_datos()
        #pero a los datos agregamos la propiedad específica de los doctores que es la especialidad
        datos["especialidad"] = self.especialidad
        return self.bd.crear(datos)

class Paciente(Persona):
    def __init__(self, nombre, edad, correo, celular, genero, notas, estatura):
        super().__init__(nombre, edad, correo, celular, genero, tipo="paciente")
        self.notas = notas
        self.estatura = estatura

    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("paciente")

    def crear (self):
        datos = self.construir_datos()
        datos["notas"] = fill(self.notas, 15) #A partir del carácter 15 cambiamos de linea (damos enter)
        datos["estatura"] = self.estatura
        return self.bd.crear(datos)
