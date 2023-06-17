# PaisDigital

Aquí hay dos programas

## I. INSTRUCCIONES PARA "RESPONDE.PY"

Este programa toma una pregunta y la responde usando la API de GPT

Para usarlo,

Ingresa tu API key (instrucciones más abajo en el código donde corresponde)
Ejecuta el siguiente comando en la terminal: python responde.py "¿Cuánto dura un día en Marte?"
O bien, si tienes Python 3.8 o superior, puedes ejecutarlo así: python3 responde.py "¿Cuánto dura un día en Marte?"

Recuerda que debes tener instalado Python, lo puedes descargar aquí: https://www.python.org/downloads/ También debes tener instalado el paquete de OpenAI, lo puedes instalar en la terminal con: pip install openai

Qué es pip? pip es el manejador de paquetes de Python, es decir, es el programa que te permite instalar paquetes de Python Si no tienes pip, puedes instalarlo con en la terminal con: python -m pip install --upgrade pip

Por último, si tienes cualquier pregunta, pregúnta a GPTChat! chat.openai.com

## II. INSTRUCCIONES PARA "GRADEFAST.PY" 

Este programa toma una rúbrica en formato .csv que debe llamarse rubric.csv y una carpeta "essays_folder" con ensayos en formato .docx (un documento para cada ensayo, indicando en su interior el nombre del autor/estudiante)

El programa calificará los ensayos en base a la rúbrica, generando un archivo para cada ensayo en la misma carpeta

Para ejecutar el programa, en la terminal ejecuta python gradefast.py
