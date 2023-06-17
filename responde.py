'''
INSTRUCCIONES:

Este programa toma una pregunta y la responde usando la API de GPT

Para usarlo, 
1. Ingresa tu API key (instrucciones más abajo en el código donde corresponde)
2. Ejecuta el siguiente comando en la terminal:
python responde.py "¿Cuánto dura un día en Marte?"

O bien, si tienes Python 3.8 o superior, puedes ejecutarlo así:
python3 responde.py "¿Cuánto dura un día en Marte?"

Recuerda que debes tener instalado Python, lo puedes descargar aquí: https://www.python.org/downloads/
También debes tener instalado el paquete de OpenAI, lo puedes instalar en la terminal con:
pip install openai

Qué es pip? pip es el manejador de paquetes de Python, es decir, es el programa que te permite instalar paquetes de Python
Si no tienes pip, puedes instalarlo con en la terminal con:
python -m pip install --upgrade pip

Por último, si tienes cualquier pregunta, pregúnta a GPTChat! chat.openai.com
'''

import argparse
import openai

# Aquí creamos el parser para recibir la pregunta del usuario
my_parser = argparse.ArgumentParser(description='Acepta una pregunta del usuario')

# Aquí agregamos los argumentos
my_parser.add_argument('Question',
                       metavar='question',
                       type=str,
                       help='la pregunta para GPT')

# Aquí ejecutamos el método parse_args() para obtener la pregunta del usuario
args = my_parser.parse_args()

preguntaUsuario = args.Question

# Aquí indican su "API key", o clave de OpenAI
# La pueden encontrar aquí: https://platform.openai.com/account/api-keys
openai.api_key = 'TU CLAVE AQUÍ, DENTRO DE LAS COMILLAS'

# Aquí definimos la función que recibe un prompt y lo manda a GPT
# Le entregamos sólo los argumentos obligatorios, el resto los dejamos por defecto
# Aquí puedes revisar los otros argumentos que podrías darle: https://platform.openai.com/docs/api-reference/chat
def llamaGPT(pregunta):
    prompt = [
        {"role": "user", "content": "Eres un asistente que responde siempre en chileno"},
        {"role": "user", "content": "Esta es la pregunta del usuario: " + pregunta},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #Aqui se puede cambiar el modelo
        messages=prompt,
    )

    # aquí imprimimos la respuesta completa de GPT
    print(f'respuesta completa: {response}') 

    # aquí imprimimos sólo el contenido de la respuesta
    contenido = response.choices[0].message["content"].strip() 
    print(f'Detalle extraído de la respuesta: {contenido}')

# Aquí llamamos a la función que definimos arriba, entregándole la pregunta del usuario
llamaGPT(preguntaUsuario)