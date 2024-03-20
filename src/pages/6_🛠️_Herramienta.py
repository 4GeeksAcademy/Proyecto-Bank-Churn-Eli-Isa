import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from pickle import load

st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>HERRAMIENTA DEL MODELO </h1>", unsafe_allow_html=True)

# Descripción de la aplicación
st.markdown("""
Esta aplicación te permite predecir si un cliente tiene probabilidad de abandono utilizando un modelo predictivo. 
Simplemente ajusta los valores de las variables a continuación y haz clic en 'Predicción' para ver el resultado.
""")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

model = load(open("Boosting_65.sav", "rb"))
scaler = joblib.load('scaler_model.joblib')

st.title("Predicción del abandono del cliente")

age = st.slider("Edad", min_value = 18.0, max_value = 100.0, step = 1.0)
active = st.selectbox("Miembro activo S/N", options=["Si","No"])
prod = st.slider("Num de productos", min_value = 0.0, max_value = 5.0, step = 1.0)
sex = st.selectbox("Sexo", options=["Hombre","Mujer"])
countries = st.selectbox("Pais", options=["Francia","Alemania", "España"])
balance = st.slider("Balance", min_value = 0.0, max_value = 250000.0, step = 10000.0)
tenure = st.slider("Antigüedad", min_value = 0.0, max_value = 10.0, step = 1.0)
cred= st.slider("Credito score", min_value = 400.0, max_value = 900.0, step = 5.0)
sal=st.slider("Salario estimado", min_value = 10.0, max_value = 200000.0, step = 2500.0)

active_n = 0 if active == 'No' else 1
sex_n= 0 if sex== 'Mujer' else 1
tenure_age=tenure/age
mem_no_prod=active_n*prod
cred_bal_sal=cred*balance/sal
bal_sal=balance/sal

if countries == 'Francia':
    countries_n = 1
elif countries == 'Alemania':
    countries_n = 2
else:
    countries_n = 3

data_for_norm=[[age, prod, active_n, sex_n, balance, countries_n, mem_no_prod,cred_bal_sal, bal_sal]]
data_norm = scaler.transform(data_for_norm)
data = [[data_norm[0][0], data_norm[0][1], data_norm[0][2], data_norm[0][3],data_norm[0][4]],data_norm[0][5],data_norm[0][6],data_norm[0][7],data_norm[0][8]]

if st.button("Predicción"):
    prediction = 'BAJA' if round(model.predict(data_norm)[0]) == 0 else 'ALTA' 
    
    st.write("¿El cliente tiene probabilidad de abandono?:", prediction)

    # Mostrar imagen según la predicción
    if prediction == 'ALTA':
        st.image("https://daxg39y63pxwu.cloudfront.net/images/blog/churn-models/Customer_Churn_Prediction_Models_in_Machine_Learning.webp", caption="PROYECTO FINAL")
    elif prediction == 'BAJA':
        st.image("https://www.sinch.com/sites/default/files/styles/small/public/image/2022-12/Os%206%20principais%20tipos%20de%20clientes%20e%20como%20lidar%20com%20cada%20um%20deles%20-%20Capa.png.webp?itok=GPuhmK6w", caption="PROYECTO FINAL")
