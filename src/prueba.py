import streamlit as st
import os
import importlib.util

# Obtener la lista de nombres de archivos en la carpeta "pages"
nombres_archivos = [nombre_archivo[:-3] for nombre_archivo in os.listdir("pages") if nombre_archivo.endswith(".py")]

# Diccionario para almacenar las funciones de cada página
paginas = {}

# Iterar sobre los nombres de los archivos y cargar los módulos
for nombre_archivo in nombres_archivos:
    # Construir la ruta al archivo
    ruta_archivo = os.path.join("pages", f"{nombre_archivo}.py")
    
    # Cargar el módulo utilizando importlib
    spec = importlib.util.spec_from_file_location(nombre_archivo, ruta_archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    
    # Agregar la función "mostrar" del módulo al diccionario de páginas
    paginas[nombre_archivo] = modulo.mostrar

# Ahora puedes acceder a las funciones de cada página
# por ejemplo, para mostrar la página "Contexto":
for nombre_pagina, funcion_mostrar in paginas.items():
    st.title(nombre_pagina.replace("_", " "))  # Reemplazar "_" con espacio para mostrar el título de la página
    funcion_mostrar()  # Llamar a la función mostrar de la página