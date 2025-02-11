import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dataset_ia.csv')

modelo = LinearRegression()

y = df[['Torque [Nm]']]
x = df[['Rotational speed [rpm]']]

modelo.fit(x,y)


st.title(f'Prevendo o Torque do motor em função do RPM')
st.divider()

rpm = st.number_input("Digite um valor de RPM: ")

if rpm:
    torque_previsto = modelo.predict([[rpm]])[0][0]
    st.write(f"{rpm:.2f} rpm gera um Torque de {torque_previsto:.2f} Nm")