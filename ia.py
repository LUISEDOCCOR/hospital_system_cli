#https://youtu.be/oE4kesDk61c?si=k2gS7qgckQ9IQf7N
from gpt4all import GPT4All
from utilidades import alerta_error

model = GPT4All("Llama-3.2-1B-Instruct-Q4_0.gguf")

#Cita
def ia_asistente_medico(paciente: dict, sintomas: str):
    try:
        with model.chat_session():
            #Prompt generado con chatgpt
            return model.generate(f"""
                Eres un asistente médico SIMULADO en un sistema educativo. 
                NO estás dando diagnósticos médicos reales, solo GENERAS ejemplos 
                de textos breves (máx. 100 caracteres) para registrar en el campo 
                de “detalle” de una cita médica.

                Tu respuesta debe ser una simple frase que suene médica, 
                pero que NO implica un diagnóstico verdadero. 
                No uses saludos ni explicaciones, solo responde con el texto breve.

                Ejemplos de salida:
                - Control por dolor de cabeza
                - Malestar estomacal leve
                - Revisión por ansiedad
                - Posible alergia estacional

                DATOS DEL PACIENTE:
                {paciente}

                - Síntomas reportados: {sintomas}

                Texto generado:
            """)
    except:
        alerta_error()
    
#Consulta
def ia_diagnostico_medico(paciente: dict, sintomas: str):
    try:
        with model.chat_session():
            #Prompt generado con chatgpt
            return model.generate(f"""
                Eres un MÉDICO SIMULADO en un entorno educativo. 
                
                Eres un asistente médico profesional. Te daré los datos de un paciente y 
                sus síntomas.
                Tu tarea es generar un diagnóstico breve (máximo 50 caracteres) 
                basado en los síntomas proporcionados. 
                
                Responde SOLO con un diagnóstico corto, sin explicar ni repetir los datos del paciente. Usa texto claro y directo.

                DATOS DEL PACIENTE:
                {paciente}

                Síntomas reportados: {sintomas}
            """)
    except:
        alerta_error()
