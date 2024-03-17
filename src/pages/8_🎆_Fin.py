import streamlit as st


# Aquí puedes agregar el contenido que deseas mostrar en la página "Contexto"
#st.title("Página de Contexto")
#st.write("Este es el contenido de la página de contexto.")
# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Sin-título-1.jpg"

# Mostrar imagen centrada y más grande
st.image(imagen_url, caption="PROYECTO FINAL", width=1200, use_column_width="always")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)