import streamlit as st
# Lista de diapositivas
slides = [
    {"title": "Contexto", 
     "content": [
        st.markdown("<h1 style='text-align: center;'>BANK CHURN PREDICTION </h1>", unsafe_allow_html=True),
        st.markdown("<h1 style='text-align: center;'>Elisa Castro</h1>", unsafe_allow_html=True),
        st.markdown("<h1 style='text-align: center;'>Isabel Estévez</h1>", unsafe_allow_html=True),
        st.markdown("<br>", unsafe_allow_html=True)
    ]},
    {"title": "Variables significativas", "content": "Contenido de la Diapositiva 2"},
    {"title": "Diapositiva 3", "content": "Contenido de la Diapositiva 3"}
    ]
# Imagen que deseas mostrar en la diapositiva
imagen_2 = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/4209212d84e0d7a26f3b308b9960360a-2.jpg"
# Índice de la diapositiva actual
slide_index = st.session_state.get("slide_index", 0)
# Mostrar la diapositiva actual
st.title(slides[slide_index]["title"])
# Mostrar la imagen en la primera diapositiva
if slide_index == 0:
    st.image(imagen_2, caption="Variables significativas")
# Mostrar el contenido de la diapositiva
st.write(slides[slide_index]["content"])
# Botón con flecha hacia la derecha para avanzar a la siguiente diapositiva
if slide_index < len(slides) - 1:
    if st.button(":flecha_a_la_derecha: Siguiente diapositiva"):
        slide_index += 1
        st.session_state["slide_index"] = slide_index
else:
    if st.button("Reiniciar presentación"):
        slide_index = 0
        st.session_state["slide_index"] = slide_index