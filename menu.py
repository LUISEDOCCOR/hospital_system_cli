#https://inquirerpy.readthedocs.io/en/latest/index.html
from InquirerPy.utils import color_print
from InquirerPy import inquirer, prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from utilidades import limpiar_consola, centrar_texto, alerta_exito, alerta_error
from preguntas import pregutas_doctor, pregutas_paciente, preguntas_persona_editar
from personas import Doctor, Persona, Paciente

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
                Choice(value=6, name="⬅️ Volver")
            ],
            default=1
        ).execute()
        datos = Doctor.obtener_todos() if tipo == "doctor" else Paciente.obtener_todos()
        match accion:
            #Crear
            case 1:
                exitoso = None
                if tipo == "doctor":
                    respuestas = prompt(pregutas_doctor)
                    exitoso = Doctor(**respuestas).crear()
                else:
                    respuestas = prompt(pregutas_paciente)
                    exitoso = Paciente(**respuestas).crear()
                if exitoso:
                    alerta_exito("Creado correctamente")
                else:
                    alerta_error()
            #Editar
            case 2:
                id = inquirer.fuzzy(
                    message = f"Selecciona el nombre del {tipo} que deseas editar:",
                    choices=[Choice(value=elemento["id"], name=elemento["nombre"]) for elemento in datos]
                ).execute()
                persona = Persona.obtener_por_id(id)
                if persona:
                    respuestas = prompt(preguntas_persona_editar(persona))
                    if Persona.editar(id, respuestas):
                        alerta_exito("Editado correctamente")
                    else:
                        alerta_error()
                else:
                    alerta_error(f"No se encontro el {tipo}")
            #Borrar
            case 3:
                id = inquirer.fuzzy(
                    message = f"Selecciona el nombre del {tipo} que deseas borrar:",
                    choices=[Choice(value=elemento["id"], name=elemento["nombre"]) for elemento in datos]
                ).execute()
                if Persona.eliminar(id):
                    alerta_exito("Eliminado correctamente")
                else:
                    alerta_error()
            #Obtener Todos
            case 4:
                for elemento in datos:
                    for clave, valor in elemento.items():
                        print(f"🔹 {clave.upper()}: {valor}")
                    print("\n")
            #Ficha
            case 5:
                id = inquirer.fuzzy(
                    message = f"Selecciona el nombre del {tipo}:",
                    choices=[Choice(value=elemento["id"], name=elemento["nombre"]) for elemento in datos]
                ).execute()
                print("\n")
                persona = Persona.obtener_por_id(id)
                if persona:
                    for clave, valor in persona.items():
                        print(f"🔹 {clave.upper()}: {valor}")
                    print("\n")
                else:
                    alerta_error(f"No se encontro el {tipo}")
            #Volver
            case 6:
                break
        input("Enter para continuar... ")

def menu_citas():
    print("Citas")

def menu_consultas():
    print("Consultas")

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
                Choice(value=3, name="📕 Citas"),
                Choice(value=4, name="📘 Consultas"),
                Separator(),
                Choice(value=5, name="📤 Salir"),
            ],
            default=1
        ).execute()
        match accion:
            case 1:
                menu_personas("doctor")
            case 2:
                menu_personas("paciente")
            case 3:
                menu_citas()
            case 4:
                menu_consultas()
            case 5:
                break
