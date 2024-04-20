import re
import random

from preguntas_respuestas import preguntas_respuestas

def responder_pregunta(pregunta):
    if pregunta in preguntas_respuestas:
        return preguntas_respuestas[pregunta]
    else:
        return "Lo siento, no puedo responder a esa pregunta."

def main():
    print("¡Hola! Soy un chatbot del ITLA. ¿En qué puedo ayudarte hoy?")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == 'adios':
            print("Cuidate por ahi")
            break
        respuesta = responder_pregunta(pregunta)
        print("Chatbot: ", respuesta)

if __name__ == "__main__":
    main()
