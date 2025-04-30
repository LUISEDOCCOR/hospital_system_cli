#https://youtu.be/oE4kesDk61c?si=k2gS7qgckQ9IQf7N
from gpt4all import GPT4All
from utilidades import alerta_error

#mac ~/.cache/gpt4all/ -> win C:\Users\TuUsuario\.cache\gpt4all\
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

#Cita
def ia_asistente_medico(paciente: dict, sintomas: str):
    try:
        with model.chat_session():
            #Prompt generado con chatgpt
            respuesta = \
            model.generate(f"""
                Eres un asistente médico SIMULADO en un sistema educativo.
                NO estás dando diagnósticos médicos reales. Tu tarea es GENERAR ejemplos de textos breves (máximo 100 caracteres)
                para registrar en el campo de “detalle” de una cita médica.

                Tu respuesta debe ser una frase simple que suene médica, escrita en español, pero que NO implique un diagnóstico verdadero.
                No incluyas saludos, explicaciones ni datos adicionales. Solo responde con el texto breve en español.

                Ejemplos de salida:
                -Control por dolor de cabeza
                -Malestar estomacal leve
                -Revisión por ansiedad
                -Posible alergia estacional

                DATOS DEL PACIENTE:
                {paciente}

                - Síntomas reportados: {sintomas}
            """)
            return respuesta if respuesta else "Error con la IA"
    except:
        alerta_error()

#Consulta
def ia_diagnostico_medico(paciente: dict, sintomas: str):
    try:
        with model.chat_session():
            #Prompt generado con chatgpt
            return model.generate(f"""
                Eres un médico simulado en un entorno educativo.
                Actúas como un asistente médico profesional.
                Se te proporcionarán los síntomas y datos relevantes de un paciente.
                Tu única tarea es generar un diagnóstico breve, de máximo 50 caracteres.

                Responde únicamente con el diagnóstico, sin explicaciones, sin repetir los datos del paciente y sin agregar ningún comentario adicional.

                Usa lenguaje médico claro, directo y conciso.

                DATOS DEL PACIENTE:
                {paciente}

                Síntomas reportados: {sintomas}
            """)
    except:
        alerta_error()
