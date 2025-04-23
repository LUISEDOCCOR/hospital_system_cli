import os, platform, shutil, time
from InquirerPy.utils import color_print
from InquirerPy import inquirer

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

def alerta_confirmar():
    return inquirer.confirm(message="Guradar cambios?", default=True).execute()
