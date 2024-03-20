import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Presentación",
    page_icon="📊"
)

# Contenido de las diapositivas
slides = [
    {
        "title": "Diapositiva 1",
        "content": [
            "## Título de la diapositiva 1",
            "Este es un texto introductorio.",
            st.image("DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/4209212d84e0d7a26f3b308b9960360a-1.jpg", caption="PROYECTO FINAL", width=1000, use_column_width="always"),
            "---"
        ]
    },
    {
        "title": "Diapositiva 2",
        "content": [
            "## Título de la diapositiva 2",
            "Este es un texto para la segunda diapositiva.",
            st.image("DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/4209212d84e0d7a26f3b308b9960360a-2.jpg", caption="PROYECTO FINAL", width=1000),
            "---"
        ]
    },
    {
        "title": "Diapositiva 3",
        "content": [
            "## Título de la diapositiva 3",
            st.image("DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/4209212d84e0d7a26f3b308b9960360a-3.jpg", caption="PROYECTO FINAL", width=1000),
            "---"
        ]
    }
]

# Índice de la diapositiva actual
slide_index = st.session_state.get("slide_index", 0)

# Mostrar la diapositiva actual
st.title(slides[slide_index]["title"])
for content in slides[slide_index]["content"]:
    st.write(content)

# Botones para avanzar y retroceder entre las diapositivas
col1, col2, col3 = st.columns([1, 10, 1])
with col2:
    st.write("")  # Espacio vacío para centrar los botones
with col1:
    if slide_index > 0:
        if st.button("← Anterior"):
            slide_index -= 1
            st.session_state["slide_index"] = slide_index
with col3:
    if slide_index < len(slides) - 1:
        if st.button("Siguiente →"):
            slide_index += 1
            st.session_state["slide_index"] = slide_index