import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h3 style='text-align: center;'>MODELO SELECIONADO: </h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color:#6fa8dc;'>Boosting Algorithms </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>(XGBOOST) </h2>", unsafe_allow_html=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/explicacion modelo.jpg"
st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width=True)

