from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.utils import color_print

opcion = inquirer.select(
    message="¿Qué deseas hacer?",
    choices=[
        Choice("Crear", name="🛠 Crear"),
        Choice("Editar", name="✏️ Editar"),
        Choice("Eliminar", name="❌ Eliminar"),
        Choice("Salir", name="🚪 Salir"),
    ]
).execute()

color_print([("fg:#00ff00", f"Elegiste: {opcion}")])
