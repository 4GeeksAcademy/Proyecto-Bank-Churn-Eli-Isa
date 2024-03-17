import streamlit as st

def mostrar():
    # Aquí puedes agregar el contenido que deseas mostrar en la página "Contexto"
    #st.title("Página de Contexto")
    #st.write("Este es el contenido de la página de contexto.")

    # Mostrar imagen debajo del título
    imagen_url = "/workspaces/Proyecto-Bank-Churn-Eli-Isa/DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Variables-1.jpg"
    st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width="always")


    # Espaciado entre los nombres
    st.markdown("<br>", unsafe_allow_html=True)