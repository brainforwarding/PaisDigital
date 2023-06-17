# PaísDigital

En este repositorio hay dos programas:
- *responde.py:* es el programa más básico que se puede desarrollar para integrarse a la API de ChatGPT. Toma una pregunta a través de la "línea de comando" (también llamada consola o terminal) y GPT la responde por la misma vía.
- *gradefast.py:* es un programa un poco más avanzado que analiza y califica muchos ensayos a la vez. Ideal para profesores que quieren ahorrar horas y horas de trabajo :)

Ambos programas hacen uso de GPT.

## I. INSTRUCCIONES PARA "RESPONDE.PY"

Este 

Para usarlo:
1. Ingresa tu API key (instrucciones más abajo en el código donde corresponde)
2. Ejecuta el siguiente comando en la terminal: python responde.py "¿Cuánto dura un día en Marte?"
(Si tienes Python 3.8 o superior, puedes ejecutarlo así: python3 responde.py "¿Cuánto dura un día en Marte?")

Debes tener instalado Python. Lo puedes descargar aquí: https://www.python.org/downloads/ 
También debes tener instalado el paquete de OpenAI, lo puedes instalar en la terminal con: pip install openai

pip es el manejador de paquetes de Python, es decir, es el programa que te permite instalar paquetes de Python Si no tienes pip, puedes instalarlo con en la terminal con: python -m pip install --upgrade pip

Si tienes cualquier duda, pregúnta a GPTChat! chat.openai.com

## II. INSTRUCCIONES PARA "GRADEFAST.PY" 

Debes ejecutar este programa desde una carpeta donde también se encuentre una rúbrica en formato .csv que debe llamarse rubric.csv y una carpeta "essays_folder" con todos los ensayos para calificar en formato .docx (un documento para cada ensayo, indicando en su interior el nombre del autor/estudiante).

El programa calificará los ensayos en base a la rúbrica, generando un archivo para cada ensayo en la misma carpeta.

Ejecuta este programa desde la terminal con: python gradefast.py
