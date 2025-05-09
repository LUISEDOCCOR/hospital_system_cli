#https://inquirerpy.readthedocs.io/en/latest/index.html
from InquirerPy.utils import color_print
from InquirerPy import inquirer, prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from utilidades import limpiar_consola, centrar_texto, alerta_exito, alerta_error, alerta_confirmar, \
selecciona_elemento_personas, mostar_tabla, selecciona_elemento_eventomedico
from preguntas import pregutas_doctor, pregutas_paciente, preguntas_persona_editar, preguntas_cita_medica, \
preguntas_consulta_medica, preguntas_eventomedico_editar
from personas import Doctor, Persona, Paciente
from eventomedico import Cita, Consulta, EventoMedico
from basededatos import Basededatos
from ia import ia_asistente_medico, ia_diagnostico_medico

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
                id = selecciona_elemento_personas(datos, f"Selecciona el nombre del {tipo} que deseas editar:")
                persona = Persona.obtener_por_id(id)
                if persona:
                    respuestas = prompt(preguntas_persona_editar(persona, tipo))
                    if alerta_confirmar():
                        if Persona.editar(id, respuestas):
                            alerta_exito("Editado correctamente")
                        else:
                            alerta_error()
                else:
                    alerta_error(f"No se encontro el {tipo}")
            #Borrar
            case 3:
                id = selecciona_elemento_personas(datos, f"Selecciona el nombre del {tipo} que deseas borrar:")
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
                id = selecciona_elemento_personas(datos, f"Selecciona el nombre del {tipo}:")
                persona = Persona.obtener_por_id(id)
                if persona:
                    mostar_tabla([persona], tipo)
                else:
                    alerta_error(f"No se encontro el {tipo}")
        input("Enter para continuar... ")

def menu_evento_medico():
    while True:
        limpiar_consola()
        tipo = inquirer.select(
            message=f"MENÚ\n",
            choices=[
                Choice(value="cita", name="🛎️ Cita"),
                Choice(value="consulta", name="💊 Consulta"),
                Choice(value=None, name="⬅️ Volver")
            ]
        ).execute()
        if not tipo:
            break
        datos = Cita.obtener_todos() if tipo == "cita" else Consulta.obtener_todos()
        limpiar_consola()
        accion = inquirer.select(
            message=f"MENÚ PARA {tipo.upper()}\n",
            choices=[
                Choice(value=1, name="🖨️ Ver todos"),
                Choice(value=2, name="✏️ Editar"),
                Choice(value=3, name="🧾 Ficha"),
                Choice(value=None, name="⬅️ Volver")
            ],
            default=1
        ).execute()
        if not accion:
            break
        match accion:
            case 1:
                mostar_tabla(datos, tipo)
            case 2:
                evento_id = selecciona_elemento_eventomedico(datos, tipo)
                eventomedico = EventoMedico.obtener_por_id(evento_id)
                if eventomedico:
                    respuestas = prompt(preguntas_eventomedico_editar(eventomedico, tipo))
                    if alerta_confirmar():
                        if EventoMedico.editar(evento_id, respuestas):
                            alerta_exito("Editado correctamente")
                        else:
                            alerta_error()
                else:
                    alerta_error(f"No se encontro la {tipo}")
            case 3:
                evento_id = selecciona_elemento_eventomedico(datos, tipo)
                eventomedico = EventoMedico.obtener_por_id(evento_id)
                if eventomedico:
                    mostar_tabla([eventomedico])
                else:
                    alerta_error(f"No se encontro la {tipo}")
        input("Enter para continuar... ")

def menu_añadir_evento_medico(tipo: str):
    doctor_id = selecciona_elemento_personas(Doctor.obtener_todos(), "Selecciona a un Doctor")
    paciente_id = selecciona_elemento_personas(Paciente.obtener_todos(), "Seleccionar a un Paciente")
    if doctor_id and paciente_id:
        respuestas = prompt(preguntas_cita_medica if tipo == "cita" else preguntas_consulta_medica)
        respuestas["doctor_id"] = doctor_id
        respuestas["paciente_id"] = paciente_id
        if alerta_confirmar(f"Usar IA para {'detalles' if tipo == 'cita' else 'el diagnostico'}"):
            if tipo == "cita":
                respuestas["detalles"] = ia_asistente_medico(Paciente.obtener_por_id(paciente_id), respuestas["motivo"])
            else:
                respuestas["diagnostico"] = ia_diagnostico_medico(Paciente.obtener_por_id(paciente_id), respuestas["motivo"])
        else:
            if tipo == "cita":
                respuestas["detalles"] = inquirer.text(message="Detalles de la cita: ").execute()
            else:
                respuestas["diagnostico"] = inquirer.text(message="Diagostico: ").execute()
        if alerta_confirmar():
            evento_id = Cita(**respuestas).crear() if tipo == "cita" else Consulta(**respuestas).crear()
            if evento_id:
                alerta_exito("Guardado correctamente")
                mostar_tabla([Cita.obtener_por_id(evento_id)])
            else:
                alerta_error()
    else:
        alerta_error("Es necesario que exista un doctor o paciente")
    input("Enter para continuar... ")

def inicio():
    limpiar_consola()
    color_print([
        ("bold fg:#00ffff", f"\n{centrar_texto('🏥 Bienvenido al sistema hospitalario 🏥')}\n"),
        ("fg:#ffffff", f"{centrar_texto('Usa las flechas ↑ ↓ para navegar y Enter para seleccionar')}\n")
    ])
    time.sleep(3)

def borrar_basededatos():
    limpiar_consola()
    x = alerta_confirmar("Seguro de borrar base de datos")
    if x:
        Basededatos.borrar_todo()
        print("Tendrás que volver a ejecutar el programa para crear nuevamente los archivos")
    return x

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
                Choice(value=6, name="⛔️ Borrar todos los datos"),
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
                menu_añadir_evento_medico("cita")
            case 4:
                menu_añadir_evento_medico("consulta")
            case 5:
                menu_evento_medico()
            case 6:
                if borrar_basededatos():
                    break
