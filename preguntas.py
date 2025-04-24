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
    },
    {
        "type": "input",
        "message": "📏 Estatura (CM):",
        "name": "estatura"
    }
]

pregutnas_evento_medico = [
    {
        "type": "input",
        "message": "📅 Fecha de la cita (YYYY-MM-DD):",
        "name": "fecha"
    },
    {
        "type": "input",
        "message": "📝 Motivo de la cita:",
        "name": "motivo"
    }
]

preguntas_cita_medica = pregutnas_evento_medico + [
    {
        "type": "list",
        "message": "📌 Estado de la cita:",
        "choices": ["Pendiente", "Terminada"],
        "name": "estado"
    }
]

def preguntas_persona_editar (valores_default: dict):
    nuevas_preguntas = deepcopy(preguntas_personas)
    for pregunta in nuevas_preguntas:
        pregunta["default"] = valores_default[pregunta["name"]]
    return nuevas_preguntas
