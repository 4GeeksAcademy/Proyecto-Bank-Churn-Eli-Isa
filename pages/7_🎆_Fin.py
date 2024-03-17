import streamlit as st


# Mostrar imagen debajo del título
imagen_url = "/workspaces/Proyecto-Bank-Churn-Eli-Isa/DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Sin-título-1.jpg"

# Mostrar imagen centrada y más grande
st.image(imagen_url, caption="PROYECTO FINAL", width=1200, use_column_width="always")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)