#https://youtu.be/oE4kesDk61c?si=k2gS7qgckQ9IQf7N
from gpt4all import GPT4All
model = GPT4All("Llama-3.2-1B-Instruct-Q4_0.gguf")
from utilidades import alerta_error


#Cita
def ia_asistente_medico(paciente: dict, sintomas: str):
    try:
        with model.chat_session():
            #Prompt generado con chatgpt
            return model.generate(f"""
            Eres un asistente médico profesional. Te daré los datos de un paciente y sus síntomas.
            Tu tarea es analizar brevemente su situación y generar una descripción concisa (máx. 50 caracteres) que resuma 
            un posible diagnóstico o situación clínica que pueda registrarse como detalle de una cita médica.
            
            
            DATOS DEL PACIENTE:
            {paciente}
            
            - Síntomas: {sintomas}
            
            Responde SOLO con una frase corta, sin explicaciones ni saludos.
            
            Ejemplos de salida:
            - Posible infección respiratoria
            - Dolor abdominal leve
            - Ansiedad leve requiere seguimiento
            - Revisión por dolor en espalda
            - Sospecha de migraña crónica
            """)
    except:
        alerta_error()
    
