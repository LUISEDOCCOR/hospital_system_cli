#https://inquirerpy.readthedocs.io/en/latest/index.html
from InquirerPy.utils import color_print
from InquirerPy import inquirer, prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from tabulate import tabulate
from utilidades import limpiar_consola, centrar_texto, alerta_exito, alerta_error, alerta_confirmar, selecciona_elemento, mostar_tabla
from preguntas import pregutas_doctor, pregutas_paciente, preguntas_persona_editar, preguntas_cita_medica
from personas import Doctor, Persona, Paciente
from eventomedico import Cita
from ia import ia_asistente_medico

def menu_personas(tipo: str):
    while True:
        limpiar_consola()
        accion = inquirer.select(
            message=f"MENÚ {tipo.upper()} \n",
            choices=[
                Choice(value=1, name="➕ Crear"),
                Choice(value=2, name="✏️ Editar"),
                Choice(value=3, name="❌ Borrar"),
                Choice(value=4, name="📋 Ver todos"),
                Choice(value=5, name="🪪 Ficha"),
                Choice(value=None, name="⬅️ Volver")
            ],
            default=1
        ).execute()
        if not accion:
            break
        datos = Doctor.obtener_todos() if tipo == "doctor" else Paciente.obtener_todos()
        match accion:
            #Crear
            case 1:
                exitoso = None
                if tipo == "doctor":
                    respuestas = prompt(pregutas_doctor)
                    if alerta_confirmar():
                        exitoso = Doctor(**respuestas).crear()
                else:
                    respuestas = prompt(pregutas_paciente)
                    if alerta_confirmar():
                        exitoso = Paciente(**respuestas).crear()
                if exitoso:
                    alerta_exito("Creado correctamente")
                else:
                    alerta_error()
            #Editar
            case 2:
                id = selecciona_elemento(datos, f"Selecciona el nombre del {tipo} que deseas editar:")
                persona = Persona.obtener_por_id(id)
                if persona:
                    respuestas = prompt(preguntas_persona_editar(persona))
                    if alerta_confirmar():
                        if Persona.editar(id, respuestas):
                            alerta_exito("Editado correctamente")
                        else:
                            alerta_error()
                else:
                    alerta_error(f"No se encontro el {tipo}")
            #Borrar
            case 3:
                id = selecciona_elemento(datos, f"Selecciona el nombre del {tipo} que deseas borrar:")
                if alerta_confirmar():
                    if Persona.eliminar(id):
                        alerta_exito("Eliminado correctamente")
                    else:
                        alerta_error()
            #Obtener Todos
            case 4:
                mostar_tabla(datos, tipo)
            #Ficha
            case 5:
                id = selecciona_elemento(datos, f"Selecciona el nombre del {tipo}:")
                persona = Persona.obtener_por_id(id)
                if persona:
                    mostar_tabla([persona], tipo)
                else:
                    alerta_error(f"No se encontro el {tipo}")
        input("Enter para continuar... ")

def menu_agendar_cita():
    doctor_id = selecciona_elemento(Doctor.obtener_todos(), "Selecciona a un Doctor")
    paciente_id = selecciona_elemento(Paciente.obtener_todos(), "Seleccionar a un Paciente")
    if doctor_id and paciente_id:
        respuestas = prompt(preguntas_cita_medica)
        respuestas["doctor_id"] = doctor_id
        respuestas["paciente_id"] = paciente_id
        if alerta_confirmar("Usar IA para los detalles"):
            respuestas["detalles"] = ia_asistente_medico(Paciente.obtener_por_id(paciente_id), respuestas["motivo"])
            if alerta_confirmar("Agendar cita?"):
                if Cita(**respuestas).crear():
                    alerta_exito("Cita agendada correctamente")
                    mostar_tabla([respuestas], "cita")
                else:
                    alerta_error()
        else:
            detalles = inquirer.text(message="Detalles de la cita: ").execute()
            respuestas["detalles"] = detalles
    else:
        alerta_error("Es necesario que exista un doctor o paciente")

    input("Enter para continuar... ")


def menu_consultas():
    print("Consultas")
    input("Enter para continuar... ")

def inicio():
    limpiar_consola()
    color_print([
        ("bold fg:#00ffff", f"\n{centrar_texto('🏥 Bienvenido al sistema hospitalario 🏥')}\n"),
        ("fg:#ffffff", f"{centrar_texto('Usa las flechas ↑ ↓ para navegar y Enter para seleccionar')}\n")
    ])
    time.sleep(3)

def mostrar_menu():
    while True:
        limpiar_consola()
        accion = inquirer.select(
            message="MENÚ \n",
            choices=[
                Choice(value=1, name="🥼 Doctores"),
                Choice(value=2, name="👤 Pacientes"),
                Separator(),
                Choice(value=3, name="📆 Agendar Cita"),
                Choice(value=4, name="📁 Registrar Consulta"),
                Choice(value=5, name="📕 Citas / Consultas"),
                Separator(),
                Choice(value=None, name="📤 Salir"),
            ],
            default=1
        ).execute()
        if not accion:
            break
        match accion:
            case 1:
                menu_personas("doctor")
            case 2:
                menu_personas("paciente")
            case 3:
                menu_agendar_cita()
            case 4:
                menu_consultas()