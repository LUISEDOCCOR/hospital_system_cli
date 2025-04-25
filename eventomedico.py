from basededatos import Basededatos
from textwrap import fill
from datetime import date

class EventoMedico:
    bd = Basededatos("eventomedico")
    def __init__(self, paciente_id, doctor_id, fecha, motivo, tipo):
        self.paciente_id = paciente_id
        self.doctor_id = doctor_id
        self.fecha = fecha
        self.motivo = motivo
        self.tipo = tipo

    def construir_datos(self):
        return {
            "paciente_id": self.paciente_id,
            "doctor_id": self.doctor_id,
            "fecha": self.fecha,
            "tipo": self.tipo,
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

class Consulta(EventoMedico):
    def __init__(self, paciente_id, doctor_id, motivo, diagnostico):
        super().__init__(paciente_id=paciente_id, doctor_id=doctor_id, motivo=motivo, fecha=(date.today().isoformat()), tipo="consulta")
        self.diagnostico = diagnostico

    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("consulta")

    def crear (self):
        datos = self.construir_datos()
        datos["diagnostico"] = fill(self.diagnostico, 40)
        datos["motivo"] = fill(self.motivo, 20)
        return self.bd.crear(datos)

        

class Cita(EventoMedico):
    def __init__(self, paciente_id, doctor_id, fecha, motivo, estado, detalles):
        super().__init__(paciente_id, doctor_id, fecha, motivo, tipo="cita")
        self.estado = estado
        self.detalles = detalles

    @classmethod
    def obtener_todos(cls, tipo=None):
        return super().obtener_todos("cita")

    def crear (self):
        datos = self.construir_datos()
        datos["estado"] = self.estado
        datos["detalles"] = fill(self.detalles, 20)
        datos["motivo"] = fill(self.motivo, 20)
        return self.bd.crear(datos)
