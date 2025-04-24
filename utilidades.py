import os, platform, shutil, time
from InquirerPy.utils import color_print
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from tabulate import tabulate
from personas import Doctor, Paciente

def limpiar_consola():
   #Si el nombre del sistema operativo es windows ejecutamos el comando cls
    if platform.system() == "Windows":
        os.system("cls")
    #Si no lo es ejecutamos el comando clear
    else:
        os.system("clear")

def centrar_texto(texto: str):
    #retornamos el texto, usamos el metodo center, que pide como argumento las columnas de la terminal
    return texto.center(shutil.get_terminal_size().columns)

def alerta_exito(mensaje: str):
    color_print([("bold fg:#00ff00", f"\n✅ {mensaje}\n")])
    time.sleep(1.5)

def alerta_error(mensaje="Hubo un error"):
    color_print([("bold fg:#ff4c4c", f"\n❌ {mensaje}\n")])
    time.sleep(1.5)

def alerta_confirmar(mensaje="Guradar cambios?"):
    return inquirer.confirm(message=mensaje, default=True).execute()

def selecciona_elemento_personas(datos: list, mensaje: str):
    if len(datos) > 0:
        return inquirer.fuzzy(
            message = mensaje,
            choices=[Choice(value=elemento["id"], name=elemento["nombre"]) for elemento in datos]
        ).execute()
    else:
        alerta_error("No hay ningun elemento para realizar esta accion")

def selecciona_elemento_eventomedico(datos: list, tipo: str):
    if len(datos) > 0:
        return inquirer.fuzzy(
            message = f"Selecciona una {tipo}",
            choices=[Choice(value=elemento["id"], 
                name=f"🥼 Doctor: {Doctor.obtener_por_id(elemento["doctor_id"])["nombre"]} 👤 Paciente: {Paciente.obtener_por_id(elemento["paciente_id"])["nombre"]} 📆 Fecha: {elemento["fecha"]}") 
                for elemento in datos
            ]
        ).execute()
    else:
        alerta_error("No hay ningun elemento para realizar esta accion")

def mostar_tabla(datos: list, tipo="elemento"):
    #https://www.datacamp.com/tutorial/python-tabulate
    if len(datos) > 0:
        print(tabulate(datos, headers="keys", tablefmt="fancy_grid", maxcolwidths=[None, 15]))
    else:
        alerta_error(f"No hay ningun {tipo} registrado")