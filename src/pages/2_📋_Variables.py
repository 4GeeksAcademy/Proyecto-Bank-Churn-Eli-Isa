import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>DESCRIPCION DE VARIABLES </h1>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("""
<h2>Lista de variables</h2>
<ul>
    <li><b>Apellido</b> del cliente</li>
    <li><b>Credit Score</b>: Puntuación de crédito, es una medida de la solvencia crediticia</li>
    <li><b>Edad</b></li>
    <li><b>Antigüedad</b> del cliente</li>
    <li><b>Balance</b></li>
    <li>Número de <b>Productos financieros</b></li>
    <li><b>Miembro activo</b></li>
    <li><b>Tarjeta</b> de crédito</li>
    <li><b>Salario</b> estimado</li>
    <li><b>Nacionalidad</b></li>
    <li><b>Sexo</b></li>
    <li><b>Baja</b> S/N (Exited)</li>
</ul>
""", unsafe_allow_html=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

