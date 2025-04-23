from copy import deepcopy

preguntas_personas = [
    {
        "type": "input",
        "message": "👤 Nombre completo:",
        "name": "nombre"
    },
    {
        "type": "input",
        "message": "🎂 Edad:",
        "name": "edad"
    },
    {
        "type": "input",
        "message": "📧 Correo electrónico:",
        "name": "correo"
    },
    {
        "type": "input",
        "message": "📱 Número de celular:",
        "name": "celular"
    },
    {
        "type": "list",
        "message": "⚧️ Género:",
        "choices": ["Masculino", "Femenino"],
        "name": "genero"
    }
]

pregutas_doctor = preguntas_personas + [
    {
        "type": "input",
        "message": "🏥 Especialidad:",
        "name": "especialidad"
    }
]

pregutas_paciente = preguntas_personas + [
    {
        "type": "input",
        "message": "🧾 Notas:",
        "name": "notas"
    }
]

def preguntas_persona_editar (valores_default: dict):
    nuevas_preguntas = deepcopy(preguntas_personas)
    for pregunta in nuevas_preguntas:
        pregunta["default"] = valores_default[pregunta["name"]]
    return nuevas_preguntas
