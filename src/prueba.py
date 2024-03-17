import streamlit as st

# Lista de diapositivas
slides = [
    {"title": "Diapositiva 1", "content": "Contenido de la Diapositiva 1"},
    {"title": "Diapositiva 2", "content": "Contenido de la Diapositiva 2"},
    {"title": "Diapositiva 3", "content": "Contenido de la Diapositiva 3"}
]

# Imagen que deseas mostrar en la diapositiva
imagen_url = "/workspaces/Proyecto-Bank-Churn-Eli-Isa/data/Comparativa balanceos.png"

# Índice de la diapositiva actual
slide_index = st.session_state.get("slide_index", 0)

# Mostrar la diapositiva actual
st.title(slides[slide_index]["title"])

# Mostrar la imagen en la primera diapositiva
if slide_index == 0:
    st.image(imagen_url, caption="Descripción de la imagen")

# Mostrar el contenido de la diapositiva
st.write(slides[slide_index]["content"])

# Botón con flecha hacia la derecha para avanzar a la siguiente diapositiva
if slide_index < len(slides) - 1:
    if st.button("➡️ Siguiente diapositiva"):
        slide_index += 1
        st.session_state["slide_index"] = slide_index
else:
    if st.button("Reiniciar presentación"):
        slide_index = 0
        st.session_state["slide_index"] = slide_index