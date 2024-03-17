import streamlit as st


# Mostrar imagen debajo del título
imagen_url = "/workspaces/Proyecto-Bank-Churn-Eli-Isa/DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Variables-1.jpg"
st.image(imagen_url, caption="PROYECTO FINAL", width=1000, use_column_width="always")


# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)