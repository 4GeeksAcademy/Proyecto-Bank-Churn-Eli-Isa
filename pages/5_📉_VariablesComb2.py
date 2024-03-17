import streamlit as st

def mostrar():
    # Aquí puedes agregar el contenido que deseas mostrar en la página "Contexto"
    #st.title("Página de Contexto")
    #st.write("Este es el contenido de la página de contexto.")
    # Mostrar imagen debajo del título
    imagen_url = "/workspaces/Proyecto-Bank-Churn-Eli-Isa/DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/4209212d84e0d7a26f3b308b9960360a-5.jpg"
    st.image(imagen_url, caption="PROYECTO FINAL", width=1000)

    # Espaciado entre los nombres
    st.markdown("<br>", unsafe_allow_html=True)