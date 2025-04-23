from basededatos import Basededatos
class Persona:
    bd = Basededatos("persona")
    def __init__(self, nombre, edad, correo, celular, genero, tipo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.celular = celular
        self.genero = genero
        self.tipo = tipo

    def construir_datos(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "correo": self.correo,
            "celular": self.celular,
            "genero": self.genero,
            "tipo": self.tipo
        }

    @classmethod
    def editar(cls, id: str, datos: dict):
        return cls.bd.editar(id, datos)

    @classmethod
    def eliminar(cls, id: str):
        return cls.bd.eliminar(id)

    @classmethod
    def obtener_por_id(cls, id: str):
        return cls.bd.obtener_por_id(id)

    @classmethod
    def obtener_todos(cls, tipo: str):
        return cls.bd.obtener_por_clave_valor("tipo", tipo)


class Doctor(Persona):
    def __init__(self, nombre, edad, correo, celular, genero, especialidad):
        super().__init__(nombre, edad, correo, celular, genero, tipo="doctor")
        self.especialidad = especialidad

    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("doctor")

    def crear (self):
        datos = self.construir_datos()
        datos["especialidad"] = self.especialidad
        return self.bd.crear(datos)

class Paciente(Persona):
    def __init__(self, nombre, edad, correo, celular, genero, notas):
        super().__init__(nombre, edad, correo, celular, genero, tipo="paciente")
        self.notas = notas

    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("paciente")

    def crear (self):
        datos = self.construir_datos()
        datos["notas"] = self.notas
        return self.bd.crear(datos)
