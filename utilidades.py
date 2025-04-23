import os, platform, shutil, time
from InquirerPy.utils import color_print

def limpiar_consola():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def centrar_texto(texto: str):
    return texto.center(shutil.get_terminal_size().columns)

def alerta_exito(mensaje: str):
    color_print([("bold fg:#00ff00", f"\n✅ {mensaje}\n")])
    time.sleep(1.5)

def alerta_error(mensaje="Hubo un error"):
    color_print([("bold fg:#ff4c4c", f"\n❌ {mensaje}\n")])
    time.sleep(1.5)
