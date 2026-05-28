import streamlit as st
import pandas as pd

df = pd.read_csv('eleitorado_por_zona_eleitoral.csv', sep=';')
st.bar_chart(df)
