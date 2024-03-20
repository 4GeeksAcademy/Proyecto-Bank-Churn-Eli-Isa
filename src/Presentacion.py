import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>BANK CHURN PREDICTION </h1>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("<h3 style='text-align: center;'>Elisa Castro</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Isabel Estévez</h3>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "https://img.freepik.com/premium-vector/bank-facade-with-tiny-people-flat-vector-illustration-office-workers-economists-making-deals-clients-exchanging-money-taking-credit-buying-house-government-finance-system-business-concept_74855-23956.jpg?w=996"

st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{imagen_url}" style="max-width: 60%;" alt="PROYECTO FINAL">
    </div>
""", unsafe_allow_html=True)

