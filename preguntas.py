from copy import deepcopy
from datetime import date

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
    },
    {
        "type": "input",
        "message": "🧭 Peso (KG):",
        "name": "peso"
    }
]

pregutnas_evento_medico = [
    {
        "type": "input",
        "message": "📝 Motivo:",
        "name": "motivo"
    }
]

preguntas_cita_medica = pregutnas_evento_medico + [
      {
        "type": "input",
        "message": "📅 Fecha de la cita (YYYY-MM-DD):",
        "name": "fecha",
        "default": date.today().isoformat()
    },
    {
        "type": "list",
        "message": "📌 Estado de la cita:",
        "choices": ["Pendiente", "Terminada"],
        "name": "estado"
    }
]


preguntas_consulta_medica = deepcopy(pregutnas_evento_medico)

def preguntas_persona_editar (valores_default: dict, tipo):
    nuevas_preguntas = deepcopy(pregutas_doctor if tipo == "doctor" else pregutas_paciente)
    for pregunta in nuevas_preguntas:
        pregunta["default"] = valores_default[pregunta["name"]]
    return nuevas_preguntas

def preguntas_eventomedico_editar (valores_default: dict, tipo):
    nuevas_preguntas = deepcopy(preguntas_cita_medica if tipo == "cita" else preguntas_consulta_medica)
    for pregunta in nuevas_preguntas:
        pregunta["default"] = valores_default[pregunta["name"]]
    return nuevas_preguntas
