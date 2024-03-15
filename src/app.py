from pickle import load
import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
import os

model = load(open("Boosting_65.sav", "rb"))
scaler = joblib.load('scaler_model.joblib')

st.title("Predicción del abandono del cliente")


age = st.slider("Edad", min_value = 18.0, max_value = 100.0, step = 1.0)
prod = st.slider("Num de productos", min_value = 0.0, max_value = 5.0, step = 1.0)
active = st.selectbox("Miembro activo S/N", options=["Si","No"])
sex = st.selectbox("Sexo", options=["Hombre","Mujer"])
balance = st.slider("Balance", min_value = 0.0, max_value = 250000.0, step = 10000.0)
countries = st.selectbox("Pais", options=["Francia","Alemania", "España"])

#Mem-no-products= active*prod
#Cred-Bal-Sal=cred*balance/sal
cred= st.slider("Credito score", min_value = 400.0, max_value = 900.0, step = 5.0)
sal=st.slider("Salario estimado", min_value = 10.0, max_value = 200000.0, step = 2500.0)
tenure = st.slider("Antigüedad", min_value = 0.0, max_value = 10.0, step = 1.0)

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
