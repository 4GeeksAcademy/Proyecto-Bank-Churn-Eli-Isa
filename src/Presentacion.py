import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>BANK CHURN PREDICTION </h1>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("<h1 style='text-align: center;'>Elisa Castro</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Isabel Estévez</h1>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "https://img.freepik.com/premium-vector/bank-facade-with-tiny-people-flat-vector-illustration-office-workers-economists-making-deals-clients-exchanging-money-taking-credit-buying-house-government-finance-system-business-concept_74855-23956.jpg?w=996"
st.image(imagen_url, caption="PROYECTO FINAL", use_column_width=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)
