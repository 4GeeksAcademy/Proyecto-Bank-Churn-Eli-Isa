import streamlit as st

# Configurar página
st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>CONTEXTO DEL PROYECTO </h1>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("""Nuestro proyecto de fin del bootcamp Data Science y Machine Learning de 4Geeks está basado en la **base de datos de un banco**, y pretende **predecir** la **probabilidad** de que un cliente se dé de **baja** o no, de cara a realizar **acciones preventivas de retención** al cliente en caso de probabilidad alta de baja.""", unsafe_allow_html=True)
st.markdown("""Para este modelo se han recopilado una serie de variables demográficas del cliente, así como otras relacionadas con la salud financiera del mismo.""", unsafe_allow_html=True)



