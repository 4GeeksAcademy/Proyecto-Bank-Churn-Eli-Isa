import streamlit as st

st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>ANÁLISIS DE VARIABLES SIGNIFICATIVAS </h1>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Variables-1.jpg"
st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)